# Script Previsão do Tempo

### Este script tem como objetivo obter dados climáticos de uma cidade por meio de uma API, salvar essas informações em um banco de dados, e permitir a consulta de previsões passadas

## Funcionalidades

* Obter dados climáticos de uma cidade específica via API
* Inserir e atualizar dados climáticos em um banco de dados
* Consultar histórico de dados climáticos armazenado no banco de dados

## Instalação

Instale as dependências

```
pip install -r requirements.txt
```

## Configuração

Adicione sua chave da API no script

```
api_key = 'chave api'
```

Crie a tabela necessária no banco de dados:

```
CREATE TABLE weather (
	id serial4 NOT NULL,
	cidade varchar(100) NULL,
	uf varchar(2) NULL,
	"data" varchar(5) NULL,
	umidade int4 NULL,
	max int4 NULL,
	min int4 NULL,
	velocidade_vento varchar(100) NULL,
	condicao varchar(100) NULL,
	probabilidade_chuva int4 NULL,
	CONSTRAINT weather_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX weather_unique_idx ON 
weather USING btree (cidade, uf, data);
```

Configure o acesso ao banco de dados no arquivo db.py

## Funções

* `main()`: Controla o fluxo principal do programa, realizando a requisição à API, processando os dados e chamando outras funções
* `get_forecast(data)`: Extrai e organiza os dados climáticos da resposta da API
* `insert_weather_data(weather_list)`: Insere os dados climáticos no banco de dados, atualizando entradas existentes conforme necessário
* `get_weather_data(city_name, uf)`: Recupera o histórico de dados climáticos do banco de dados para uma cidade e estado específicos