# database.py
from os import getenv
from dotenv import load_env
from psycopg import connect, OperationalError
from sys import exit

load_env()

def connect_to_database():
    try:
        conn = connect(
            host=getenv('DB_HOSTNAME'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD')
        )
        cur = conn.cursor()
    except OperationalError:
        print("Error: Could not connect to the database.")
        exit(1)
    return conn, cur

def check_table_exists():
    conn, cur = connect_to_database()
    cur.execute("SELECT sentiscore FROM pg_database;")
    list_database = cur.fetchall()
    conn.close()
    return ('sentiscore',) in list_database

def create_database():
    conn, cur = connect_to_database()
    cur.execute('CREATE TABLE sentiscore (id serial PRIMARY KEY,'
                                'post_id VARCHAR(255) UNIQUE,'
                                'post_text TEXT,'
                                'created_at TIMESTAMP,'
                                'user_id VARCHAR(255),'
                                'user_name VARCHAR(15),'
                                'user_profile_image_url VARCHAR(255),'
                                'retweet_count INT,'
                                'like_count INT);'
                                )
    conn.commit()
