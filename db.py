import psycopg2
import psycopg2.extras

def get_db_connection():
    conn = psycopg2.connect(
        host="db_postgresql",
        port="5432",
        dbname="main_db",
        user="admin",
        password="admin123"
    )
    return conn