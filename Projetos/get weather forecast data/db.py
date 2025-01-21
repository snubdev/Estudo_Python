import psycopg2

def get_db_config():
    try:
        conn = psycopg2.connect(
            dbname = "",
            user = "",
            password = "",
            host = "",
            port = ""
        )

        #print("Conexão estabelecida com sucesso!")

        return conn
    except Exception as e:
        return f'Ocorreu um erro: {e}'
