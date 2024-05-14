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

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def define_valid_fields():
    # Get Twitter v2 API valid fields
    valid_tweet_fields = ['attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'public_metrics', 'organic_metrics', 'promoted_metrics', 'possibly_sensitive', 'referenced_tweets', 'reply_settings', 'source', 'text', 'withheld']
    valid_expansions = ['attachments.poll_ids', 'attachments.media_keys', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id']
    valid_media_fields = ['duration_ms', 'height', 'media_key', 'preview_image_url', 'type', 'url', 'width', 'public_metrics', 'non_public_metrics', 'organic_metrics', 'promoted_metrics', 'alt_text', 'variants']
    valid_place_fields = ['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']
    valid_poll_fields = ['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']
    valid_user_fields = ['created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'verified_type', 'withheld']

    return valid_tweet_fields, valid_expansions, valid_media_fields, valid_place_fields, valid_poll_fields, valid_user_fields

def define_query_params(request_args, valid_fields):
    query_params = {}
    for field, valid_field in valid_fields.items():
        fields = [f for f in request_args.get(field, default = '', type = str).split(',') if f]
        if all(f in valid_field for f in fields):
            query_params[field] = fields
    return query_params

def check_fields(request_args, valid_fields):
    for field, valid_field in valid_fields.items():
        fields = [f for f in request_args.get(field, default = '', type = str).split(',') if f]
        if not all(f in valid_field for f in fields):
            return f"Invalid {field} value(s) provided."
    return None

@app.route('/2/tweets', methods=['GET'])
def get_posts():
    # Load replicate api data
    posts = load_json('posts.json')

    # Get the 'ids" query parameter from request
    ids_param = request.args.get('ids', default = '1', type = str)

    # Split the parameter into a list of IDs
    ids = [int(id) for id in ids_param.split(',')]

    valid_tweet_fields, valid_expansions, valid_media_fields, valid_place_fields, valid_poll_fields, valid_user_fields = define_valid_fields()

    valid_fields = {
        'tweet.fields': valid_tweet_fields,
        'expansions': valid_expansions,
        'media.fields': valid_media_fields,
        'place.fields': valid_place_fields,
        'poll.fields': valid_poll_fields,
        'user.fields': valid_user_fields
    }

    # Define query parameters and check if requested fields are valid for each field
    requested_fields = {}
    for field, valid_field in valid_fields.items():
        query_params = define_query_params(request.args, {field: valid_field})
        requested_fields[field] = query_params.get(field, [])
        error = check_fields(request.args, {field: valid_field})
        if error:
            return jsonify({"error": error}), 400

    # Find the posts with the given IDs
    responses = []
    for post in posts['data']:
        if int(post['id']) in ids:
            # Create a response for each post
            response = {field: post[field] for field in post if field in requested_fields['tweet.fields'] and field in valid_fields['tweet.fields']}

            # Add expansions to the response
            for expansion in valid_expansions:
                parts = expansion.split('.')
                current = post
                for part in parts:
                    if part in current:
                        current = current[part]
                    else:
                        current = None
                        break
                if current is not None and expansion in requested_fields['expansions']:
                    response[expansion] = current

            # Add additional fields to the response
            if 'media' in posts['includes'] and 'attachments.media_keys' in valid_expansions:
                response['media'] = [{field: media[field] for field in media if field in requested_fields['media.fields']} for media in posts['includes']['media']]

            if 'places' in posts['includes'] and 'geo.place_id' in valid_expansions:
                response['places'] = [{field: place[field] for field in place if field in requested_fields['place.fields']} for place in posts['includes']['places']]

            if 'polls' in posts['includes'] and 'attachments.poll_ids' in valid_expansions:
                response['polls'] = [{field: poll[field] for field in poll if field in requested_fields['poll.fields']} for poll in posts['includes']['polls']]

            if 'users' in posts['includes'] and 'author_id' in valid_expansions and 'author_id' in requested_fields['expansions']:
                for user in posts['includes']['users']:
                    if str(user['id']) == str(post['author_id']):
                        # Only include the fields specified in 'user.fields' query parameter
                        response['author'] = {field: user[field] for field in user if field in requested_fields['user.fields']}

            responses.append(response)

    return jsonify(responses)

@app.route('/2/tweets/<int:id>', methods=['GET'])
def get_post(id):
    # Load replicate api data
    posts = load_json('posts.json')

    # Get the query paramaters from request
    id = request.args.get('id', default = 1, type = int)

    valid_tweet_fields, valid_expansions, valid_media_fields, valid_place_fields, valid_poll_fields, valid_user_fields = define_valid_fields()

    valid_fields = {
        'tweet.fields': valid_tweet_fields,
        'expansions': valid_expansions,
        'media.fields': valid_media_fields,
        'place.fields': valid_place_fields,
        'poll.fields': valid_poll_fields,
        'user.fields': valid_user_fields
    }

    define_query_params(request.args, valid_fields)

    # Check if requested fields are valid
    error = check_fields(request.args, valid_fields)
    if error:
        return jsonify({"error": error}), 400

    # Find the post with the given ID
    for post in posts['data']:
        if int(post['id']) == id:


            return jsonify(response)

    # if no post with given ID, return 404 error
    abort(404)

if __name__ == '__main__':
    initialize_server()
