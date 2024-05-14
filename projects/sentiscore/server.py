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
    tweet_fields = [field for field in request.args.get('tweet.fields', default = '', type = str).split(',') if field]
    media_fields = [field for field in request.args.get('media.fields', default = '', type = str).split(',') if field]
    place_fields = [field for field in request.args.get('place.fields', default = '', type = str).split(',') if field]
    poll_fields = [field for field in request.args.get('poll.fields', default = '', type = str).split(',') if field]
    user_fields = [field for field in request.args.get('user.fields', default = '', type = str).split(',') if field]

    # Define valid fields
    valid_tweet_fields = ['attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'public_metrics', 'organic_metrics', 'promoted_metrics', 'possibly_sensitive', 'referenced_tweets', 'reply_settings', 'source', 'text', 'withheld']
    valid_media_fields = ['duration_ms', 'height', 'media_key', 'preview_image_url', 'type', 'url', 'width', 'public_metrics', 'non_public_metrics', 'organic_metrics', 'promoted_metrics', 'alt_text', 'variants']
    valid_place_fields = ['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']
    valid_poll_fields = ['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']
    valid_user_fields = ['created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'verified_type', 'withheld']

    # Check if all provided fields are valid
    if not all(field in valid_tweet_fields for field in tweet_fields):
        return jsonify({"error": "Invalid tweet field provided"}), 400
    if not all(field in valid_media_fields for field in media_fields):
        return jsonify({"error": "Invalid media field provided"}), 400
    if not all(field in valid_place_fields for field in place_fields):
        return jsonify({"error": "Invalid place field provided"}), 400
    if not all(field in valid_poll_fields for field in poll_fields):
        return jsonify({"error": "Invalid poll field provided"}), 400
    if not all(field in valid_user_fields for field in user_fields):
        return jsonify({"error": "Invalid user field provided"}), 400

    with open('posts.json', 'r') as f:
        posts = json.load(f)
    # Find the post with the given ID
    for post in posts['data']:
        if int(post['id']) == id:
            # Create a new dictionary with only the requested fields
            response = {field: post[field] for field in tweet_fields if field in post}
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
