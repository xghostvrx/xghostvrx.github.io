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
