from dotenv import load_dotenv
from os import getenv
import psycopg

# Load environemtn variables from .env file
load_dotenv()

# Access environmental variables
db_hostname = getenv('DB_HOSTNAME')
db_name = getenv('DB_NAME')
db_username = getenv('DB_USERNAME')
db_password = getenv('DB_PASSWORD')

# Connect to an existing database
with psycopg.connect(
    host=db_hostname,
    dbname=db_name,
    user=db_username,
    password=db_password
) as conn:
    with conn.cursor() as cur:
        # Execute a command: this creates a new table
        cur.execute('DROP TABLE IF EXISTS sentiscore;')
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
