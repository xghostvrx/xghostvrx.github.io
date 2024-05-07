# server.py
import logging
import json
from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, abort
from database import check_columns, check_database_exists, create_database, check_table_exists, create_table, drop_table

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
def get_post():
    id = request.args.get('id', default = 1, type = int)
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    # Find the post with the given ID
    for post in posts['data']:
        if post['id'] == id:
            return jsonify(post)
    # If no post with given ID, return 404 error
    abort(404)

if __name__ == '__main__':
    initialize_server()
