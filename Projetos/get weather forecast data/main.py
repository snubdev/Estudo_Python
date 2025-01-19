import json
import requests
from db import *

api_key = ''

def main():
    # Define a cidade e estado para a consulta na API
    city_name = 'São Paulo'
    uf = 'SP'

    # Substitui espaços no nome da cidade por underscores
    city_name = city_name.replace(' ', '_')

    url = f'https://api.hgbrasil.com/weather?key={api_key}&city_name={city_name},{uf}'

    # Faz uma requisição GET para obter os dados da API
    response = requests.get(url)

    if response.status_code == 200:
        # Converte a resposta em JSON
        data = response.json()

        if 'results' in data:
            # Cria uma lista com os dados da API e imprime as informações climáticas do dia atual
            weather_list = get_forecast(data)

            # Insere os dados climáticos no banco de dados
            insert_weather_data(weather_list)

            # Busca no banco o histórico dos dados climáticos
            data_weather = get_weather_data(city_name, uf)

            print()
            print('Histórico de previsões')
            # Exibe as previsões históricas
            for d in data_weather:
                print(f'{d[0]} - umidade:{d[1]}% - max:{d[2]} - min:{d[3]}')
        else:
            print('Erro: Dados não encontrados na resposta da API')
    else:
        # Exibe uma mensagem de erro se a requisição falhar
        print(f'Erro ao acessar a API: {response.status_code}')

# Processa a resposta da API para extrair os dados da previsão do tempo
def get_forecast(data):
    city_uf = data['results']['city']
    print(city_uf)
    city_uf = city_uf.split(",")
    city_name = city_uf[0]
    uf = city_uf[1].strip(" ")

    weather_forecast = data['results']['forecast']

    print(f'{weather_forecast[0]["weekday"]}({weather_forecast[0]["date"]}) - umidade:{weather_forecast[0]["humidity"]}% - max:{weather_forecast[0]["max"]} - min:{weather_forecast[0]["min"]}')

    weather_list = []

    for f in weather_forecast:
        weather_list.append({
            "city_name": city_name,
            "state": uf,
            "date": f["date"],
            "humidity": f["humidity"],
            "max": f["max"],
            "min": f["min"],
            "rain_probability": f["rain_probability"],
            "wind_speedy": f["wind_speedy"],
            "condition": f["condition"]
        })

    return weather_list

# Insere os dados climáticos no banco de dados
def insert_weather_data(weather_list):
    con = get_db_config()
    cur = con.cursor()

    query = f"""INSERT INTO weather (cidade, uf, data, umidade, max, min, velocidade_vento, condicao, probabilidade_chuva)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (cidade, uf, data) DO UPDATE
                SET umidade = EXCLUDED.umidade,
                max = EXCLUDED.max,
                min = EXCLUDED.min,
                velocidade_vento = EXCLUDED.velocidade_vento,
                condicao = EXCLUDED.condicao,
                probabilidade_chuva = EXCLUDED.probabilidade_chuva;"""

    data_weather = [
        (
            weather["city_name"],
            weather["state"],
            weather["date"],
            weather["humidity"],
            weather["max"],
            weather["min"],
            weather["wind_speedy"],
            weather["condition"],
            weather["rain_probability"]
        )
        for weather in weather_list
    ]

    cur.executemany(query, data_weather)
    con.commit()

    print()
    print('Dados inserido com sucesso')

# Recupera os dados climáticos históricos do banco de dados
def get_weather_data(city_name, uf):
    con = get_db_config()
    cur = con.cursor()

    city_name = city_name.replace('_', ' ')

    query = """SELECT data, umidade, max, min FROM weather
               WHERE cidade = %s AND uf = %s;"""

    cur.execute(query, (city_name, uf))
    result = cur.fetchall()

    return result


if __name__ == '__main__':
    main()