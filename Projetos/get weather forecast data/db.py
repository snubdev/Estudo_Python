import psycopg2

def get_db_config():
    try:
        conn = psycopg2.connect(
            dbname = "weekly_project",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "5432"
        )

        #print("Conexão estabelecida com sucesso!")

        return conn
    except Exception as e:
        return f'Ocorreu um erro: {e}'
