# database.py
from os import getenv
from dotenv import load_env
from psycopg import connect, OperationalError
from sys import exit

load_env()

def connect_to_server():
    try:
        conn = connect(
            host=getenv('DB_HOSTNAME'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD')
        )
        cur = conn.cursor()
    except:
        print("Error: Could not connect to the server.")
        exit(1)
    return conn, cur

def connect_to_database():
    try:
        conn = connect(
            host=getenv('DB_HOSTNAME'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD'),
            dbname='sentiscore'
        )
        cur = conn.cursor()
    except OperationalError:
        print("Error: Could not connect to the 'sentiscore' database.")
        exit(1)
    return conn, cur

def check_database_exists():
    conn, cur = connect_to_server()
    try:
        cur.execute("""
            SELECT EXISTS (
                SELECT datname FROM pg_database
                WHERE datname = 'sentiscore'
            );
        """)
        database_exists = cur.fetchone()[0]
    except OperationalError:
        print("Error: Could not check if database exists.")
        exit(1)
    finally:
        conn.close()
    return database_exists

def create_database():
    conn, cur = connect_to_database()
    conn.set_session(autocommit=True)
    try:
        cur.execute('CREATE DATABASE sentiscore;')
    except OperationalError:
        print("Error: Could not create 'sentiscore' database.")
        exit(1)

def create_table():
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
