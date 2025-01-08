import os
import json
import requests

# Chave de Acesso da API
api_key = ''
url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR'

def main():
    # Faz uma requisição GET para obter os dados da API
    response = requests.get(url)
    if response.status_code == 200:
        # Converte a resposta em JSON
        data = response.json()

        # Define o nome do arquivo para salvar os dados
        file_name = 'payload.json'
        # Cria um arquivo JSON com os dados da API
        create_json(file_name, data)

        # Faz a leitura dos dados do arquivo JSON
        data_films = open_json(file_name)

        # Exibe a lista de filmes ordenada alfabeticamente
        print('Lista de Filmes em Ordem Alfabética')
        display_json(data_films)

        # Exemplo de pesquisa de filmes (atualmente com título vazio)
        title = ''
        print(search_json(title, data_films))

        # Exemplo de atualização de dados de um filme
        title_up = 'teste'
        score = 'teste'
        year = 'teste'

        # Atualiza o JSON com novos dados
        updade_movies = update_json(file_name, data_films, title_up, score, year)
        print(updade_movies)
    else:
        # Exibe uma mensagem de erro se a requisição falhar
        print(f'Erro ao acessar a API: {response.status_code}')

# Cria um arquivo JSON com os dados fornecidos pela API
def create_json(file_name, data):
    new_data = {'filmes': []}

    for movie in data['results']:
        new_data['filmes'].append({
            "título": movie['title'],
            "nota": movie['vote_average'],
            "ano de Lançamento": movie['release_date']
        })

    result = save_json(file_name, new_data)

    return result

# Abre um arquivo JSON e carrega seus dados
def open_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

# Salva os dados fornecidos em um arquivo JSON
def save_json(file_name, data):
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{file_name} salvo com sucesso')

# Exibe a lista de filmes em ordem alfabética
def display_json(data_films):
    list_ordered_titles = []
    for d in data_films['filmes']:
        list_ordered_titles.append(d['título'])

    ordered_titles = sorted(list_ordered_titles)

    for title in ordered_titles:
         print(title)

    return ordered_titles

# Pesquisa um filme pelo título no JSON
def search_json(title, data_films):
    if title:
        for film in data_films["filmes"]:
                if film["título"].lower() == title.lower():
                    print(film)
                    return film
                else:
                    film = "Nenhum filme encontrado"
                    return film
    else:
        return 'Título vazio'

# Atualiza o JSON com novos dados de filmes
def update_json(file, data_films, title, score, year):
    if title and score and year:
        data_films['filmes'].append({
            "título": title,
            "nota": score,
            "ano de Lançamento": year
        })

        save_json(file, data_films)
    else:
        return 'title, score e year vazio'


if __name__ == '__main__':
    main()