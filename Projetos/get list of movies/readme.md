# Script Catálogo de Filmes

### O script tem como principal objetivo interagir com uma API para obter uma lista de filmes, armazená-la em um arquivo JSON, exibir e atualizar os dados.

## Funcionalidades

* Obter a lista de filmes mais bem avaliados via API do TMDb
* Salvar a lista de filmes em um arquivo JSON
* Exibir a lista de filmes ordenada alfabeticamente
* Buscar filmes por título no arquivo JSON
* Atualizar a lista de filmes com novos dados

## Configuração

Adicione sua chave da API no script main.py:

```
api_key = 'chave_api'
```

## Funções

* `main()`: Controla o fluxo principal do programa, realizando a requisição à API, processando os dados e chamando outras funções.
* `create_json(file_name, data)`: Cria um arquivo JSON com os dados fornecidos pela API.
* `open_json(file)`: Abre um arquivo JSON e carrega seus dados.
* `save_json(file_name, data)`: Salva os dados fornecidos em um arquivo JSON.
* `display_json(data_films)`: Exibe a lista de filmes em ordem alfabética.
* `search_json(title, data_films)`: Pesquisa um filme pelo título no JSON.
* `update_json(file, data_films, title, score, year)`: Atualiza o JSON com novos dados de filmes.