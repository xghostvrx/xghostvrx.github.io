from os import getenv
from psycopg import connect, OperationalError
import logging

def connect_to_server():
    try:
        conn = connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD')
        )
        cur = conn.cursor()
        return conn, cur
    except OperationalError as e:
        logging.error(f"Error: Could not connect to the database server. {e}")
        exit(1)

def connect_to_database(db_name):
    try:
        conn = connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USERNAME'),
            password=getenv('DB_PASSWORD'),
            dbname=db_name
        )
        cur = conn.cursor()
        return conn, cur
    except OperationalError as e:
        logging.error(f"Error: Could not connect to the '{db_name}' database. {e}")
        exit(1)

def check_database_exists(db_name):
    conn, cur = connect_to_server()
    try:
        cur.execute("SELECT EXISTS (SELECT datname FROM pg_database WHERE datname = %s)", (db_name,))
        return cur.fetchone()[0]
    except OperationalError as e:
        logging.error(f"Error: Could not check if database exists. {e}")
        exit(1)
    finally:
        conn.close()

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
        return cur.fetchone()[0]
    except OperationalError as e:
        logging.error(f"Error: Could not check if table exists. {e}")
        exit(1)
    finally:
        conn.close()

def check_columns(db_name):
    conn, cur = connect_to_database(db_name)
    columns_to_check = ['id', 'created_at', 'author_id', 'name', 'username', 'description', 'text', 'polarity', 'subjectivity', 'sentiment']
    try:
        for column in columns_to_check:
            cur.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public'
                AND table_name = 'posts'
                AND column_name = %s
            """, (column,))
            if cur.fetchone() is None:
                logging.warning(f"Column '{column}' does not exist.")
                return False
        return True
    except OperationalError as e:
        logging.error(f"Error: Could not check if columns exist. {e}")
        exit(1)
    finally:
        conn.close()

def create_database(db_name):
    conn, cur = connect_to_server()
    conn.autocommit = True
    try:
        cur.execute(f"CREATE DATABASE {db_name};")
    except OperationalError as e:
        logging.error(f"Error: Could not create '{db_name}' database. {e}")
        exit(1)
    finally:
        conn.close()

def create_table(db_name):
    conn, cur = connect_to_database(db_name)
    try:
        cur.execute('CREATE TABLE posts (id VARCHAR(255) PRIMARY KEY,'
                    'created_at TIMESTAMP,'
                    'author_id VARCHAR(255),'
                    'name VARCHAR(50),'
                    'username VARCHAR(15),'
                    'description TEXT,'
                    'text TEXT,'
                    'polarity REAL,'
                    'subjectivity REAL,'
                    'sentiment VARCHAR(10));'
                    )
        conn.commit()
    except OperationalError as e:
        logging.error(f"Error: Could not create 'posts' table. {e}")
        exit(1)
    finally:
        conn.close()

def drop_table(db_name):
    conn, cur = connect_to_database(db_name)
    try:
        cur.execute("DROP TABLE IF EXISTS posts;")
        conn.commit()
    except OperationalError as e:
        logging.error(f"Error: Could not drop 'posts' table. {e}")
        exit(1)
    finally:
        conn.close()

def insert_post(db_name, post, user):
    conn, cur = connect_to_database(db_name)
    try:
        cur.execute("""
            INSERT INTO posts (id, created_at, author_id, name, username, description, text, polarity, subjectivity, sentiment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (post.get('id'), post.get('created_at'), post.get('author_id'), user.get('name'), user.get('username'), user.get('description'), post.get('text'), post.get('polarity'), post.get('subjectivity'), post.get('sentiment')))
        conn.commit()
    except OperationalError as e:
        logging.error(f"Error: Could not insert post into 'posts' table. {e}")
    finally:
        conn.close()
