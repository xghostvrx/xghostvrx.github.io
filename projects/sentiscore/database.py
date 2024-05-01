# database.py
import psycopg
from os import getenv
from dotenv import load_env

load_env()

def connect_to_database():
    conn = psycopg.connect(
        host=getenv('DB_HOSTNAME'),
        user=getenv('DB_USERNAME'),
        password=getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    return conn, cur

def check_database_exists():
    conn, cur = connect_to_database()
    cur.execute("SELECT sentiscore FROM pg_database;")
    list_database = cur.fetchall()
    conn.close()
    return ('sentiscore',) in list_database
