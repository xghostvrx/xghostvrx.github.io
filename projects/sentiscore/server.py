import logging
from os import getenv
from dotenv import load_dotenv
from flask import Flask
from database import check_columns, check_database_exists, create_database, check_table_exists, create_table, drop_table

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

load_dotenv(override=True)

app = Flask(__name__)

def initialize_server():
    db_name = getenv('DB_NAME')
    try:
        if not check_database_exists(db_name):
            logging.info(f"Database '{db_name}' does not exist. Creating database.")
            create_database(db_name)

        if not check_table_exists(db_name):
            logging.info("'posts' table does not exist. Creating table.")
            create_table(db_name)

        if not check_columns(db_name):
            logging.warning("Data columns in 'posts' table do not appear to be appropriate. Dropping and recreating the table.")
            drop_table(db_name)
            create_table(db_name)

    except Exception as e:
        logging.error(f"An error occurred while initializing the server: {e}")
        exit(1)

    logging.info('The application has passed initialization checks.')
    logging.info('Running the server application.')
    app.run()

if __name__ == '__main__':
    initialize_server()

