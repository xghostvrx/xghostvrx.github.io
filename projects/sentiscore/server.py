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
    # Get the query parameters from request
    id = request.args.get('id', default = 1, type = int)
    tweet_fields = request.args.get('tweet.fields', default = '', type = str).split(',')
    media_fields = request.args.get('media.fields', default = '', type = str).split(',')
    place_fields = request.args.get('place.fields', default = '', type = str).split(',')
    poll_fields = request.args.get('poll.fields', default = '', type = str).split(',')
    user_fields = request.args.get('user.fields', default = '', type = str).split(',')
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    # Find the post with the given ID
    for post in posts['data']:
        if post['id'] == id:
            # Create a new dictionary with only the requested fields
            response = {field: post [field] for field in tweet_fields if field in post}
            # Add additional fields to the response
            if 'includes' in post:
                includes = post['includes']
                if 'media' in includes:
                    response['media'] = {field: includes['media'][field] for field in media_fields if field in includes['media']}
                if 'places' in includes:
                    response['places'] = {field: includes['places'][field] for field in place_fields if field in includes['places']}
                if 'polls' in includes:
                    response['polls'] = {field: includes['polls'][field] for field in poll_fields if field in includes['polls']}
                if 'users' in includes:
                    response['users'] = {field: includes['users'][field] for field in user_fields if field in includes['users']}
            return jsonify(response)
    # If no post with given ID, return 404 error
    abort(404)

if __name__ == '__main__':
    initialize_server()
