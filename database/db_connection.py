import psycopg2
from psycopg2 import OperationalError

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(dbname='delivery',
                                user = 'postgres',
                                password = 'manal2000',
                                host = 'localhost',
                                port = '5432'
                                )
        print("Connection to PostgreSQL DB successful")
        return conn
    except OperationalError as e:
        print(f"Error {e} occurred while connecting to PostgreSQL")
        return None
