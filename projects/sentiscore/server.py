# server.py
import logging
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template
from database import check_columns, check_database_exists, create_database, check_table_exists, create_table, drop_table
from x_api_mock import get_post, get_posts

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

load_dotenv(override=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def initialize_server():
    db_name = getenv('DB_NAME')
    if not check_database_exists(db_name):
        logging.info(f"Database '{db_name}' does not exist.")
        logging.info(f"Creating '{db_name}' database.")
        create_database(db_name)

    elif not check_table_exists(db_name):
        logging.info("'posts' table does not exists.")
        logging.info("Creating 'posts' table.")
        create_table(db_name)

    elif not check_columns(db_name):
        logging.warning("Data columns in 'posts' table do not appear to be appropriate.")
        logging.warning("Dropping the 'posts' table and creating a new one.")
        drop_table(db_name)
        create_table(db_name)

    logging.info('The application has passed initialization checks.')
    logging.info('Running the application and its server as intented.')
    app.run()

@app.route('/2/tweets', methods=['GET'])
def post_lookup_by_IDs():
    return get_posts()

@app.route('/2/tweets/<id>', methods=['GET'])
def post_lookup_by_ID(id):
    return get_post(id)

if __name__ == '__main__':
    initialize_server()
