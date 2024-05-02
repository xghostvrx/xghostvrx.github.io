# database.py
from os import getenv
from psycopg import connect, OperationalError
from sys import exit

def connect_to_server():
    try:
        conn = connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD')
        )
        cur = conn.cursor()
    except:
        print("Error: Could not connect to the database server.")
        exit(1)
    return conn, cur

def connect_to_database(db_name):
    try:
        conn = connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD'),
            dbname=db_name
        )
        cur = conn.cursor()
    except OperationalError:
        print(f"Error: Could not connect to the '{db_name}' database.")
        exit(1)
    return conn, cur

def check_database_exists(db_name):
    conn, cur = connect_to_server()
    try:
        cur.execute("""
            SELECT EXISTS (
                SELECT datname FROM pg_database WHERE datname = %s
            )
        """, (db_name,))
        database_exists = cur.fetchone()[0]
    except OperationalError:
        print("Error: Could not check if database exists.")
        exit(1)
    finally:
        conn.close()
    return database_exists

def check_table_exists(db_name):
    conn, cur = connect_to_database(db_name)
    try:
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = 'posts'
            );
        """)
        table_exists = cur.fetchone()[0]
    except OperationalError:
        print("Error: Could not check if table exists.")
        exit(1)
    finally:
        conn.close()
    return table_exists

def check_columns(db_name):
    conn, cur = connect_to_database(db_name)
    columns_to_check = ['id', 'post_id', 'post_text', 'created_at', 'user_id', 'user_name', 'user_profile_image_url', 'retweet_count', 'like_count']
    try:
        for column in columns_to_check:
            cur.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public'
                AND table_name = 'posts'
                AND column_name = %s
            """, (column,))
            result = cur.fetchone()
            if result is None:
                print(f"Column '{column}' does not exist.")
                return False
        return True
    except OperationalError:
        print("Error: Could not check if columns exist.")
        exit(1)
    finally:
        conn.close()

def create_database(db_name):
    conn, cur = connect_to_server()
    conn.autocommit = True
    try:
        cur.execute(f"CREATE DATABASE {db_name};")
    except OperationalError:
        print(f"Error: Could not create '{db_name}' database.")
        exit(1)

def create_table(db_name):
    conn, cur = connect_to_database(db_name)
    cur.execute('CREATE TABLE posts (id serial PRIMARY KEY,'
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

def drop_table(db_name):
    conn, cur = connect_to_database(db_name)
    try:
        cur.execute("DROP TABLE IF EXISTS posts;")
        conn.commit()
    except OperationalError:
        print("Error: Could not drop 'posts' table.")
        exit(1)
    finally:
        conn.close()

