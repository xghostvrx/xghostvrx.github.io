import logging, json
from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from textblob import TextBlob
from database import check_columns, check_database_exists, create_database, check_table_exists, create_table, drop_table, insert_post

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

load_dotenv(override=True)

app = Flask(__name__)

# Initialize sever and check if the database and table exist
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
    app.run(debug=True)


# Load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Analyze sentiment of a text
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    if polarity > 0:
        sentiment_class = 'positive'
    elif polarity < 0:
        sentiment_class = 'negative'
    else:
        sentiment_class = 'neutral'

    return {
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sentiment': sentiment_class
    }

# Predefined dictionary with acceptable keys and values
# The keys are the acceptable arguments that can be passed in the request
# The values are either a list of acceptable values or a function that validates the argument value
acceptable_args = {
    'ids': lambda x: x.isdigit() and len(x) == 19,
    'tweet.fields': ['author_id', 'created_at', 'id', 'text'],
    'user.fields': ['created_at', 'description', 'id', 'name', 'username']
}

# Define the index
@app.route('/')
def index():
    return render_template('index.html')

# Define endpoint for GET requests
@app.route('/tweets', methods=['GET'])
def get_posts():
    # Get request arguments
    args = request.args.to_dict()

    # Validate request arguments
    errors = []
    for key, string in args.items():
        values = string.split(',')
        if key not in acceptable_args:
            errors.append(f"Invalid argument: {key}")
            continue  # Skip further checks for this key since it's already invalid
        if isinstance(acceptable_args[key], list):  # Check if the acceptable value is a list
            for value in values:
                if value not in acceptable_args[key]:
                    errors.append(f"Invalid argument value: {key}={value}")
        elif callable(acceptable_args[key]):  # Check if the acceptable value is a function
            for value in values:
                if not acceptable_args[key](value):  # Call the function with the value
                    errors.append(f"Invalid argument value: {key}={value}")

    if errors:
        return jsonify({"error": errors}), 400

    # Parse additional arguments (if in the request)
    tweet_fields = args.get('tweet.fields', '').split(',')
    user_fields = args.get('user.fields', '').split(',')
    if tweet_fields:
        args['tweet.fields'] = tweet_fields
    if user_fields:
        args['user.fields'] = user_fields

    # Filter posts based on 'ids' argument
    object = load_json('posts.json')
    filtered_posts = []
    filtered_users = []
    if 'ids' in args:
        ids = args['ids'].split(',')
        ids = [int(id) for id in ids]
        for index in object['data']:
            if index['id'] in ids:
                # Include the specified tweet fields (if requested in the arguments)
                filtered_post = {key: index[key] for key in tweet_fields if key in index} if tweet_fields else index

                # Include the specified user fields (if requested in the arguments)
                author_id = index['author_id']
                for user in object['includes']['users']:
                    if user['id'] == author_id:
                        filtered_user = {key: user[key] for key in user_fields if key in user} if user_fields else user
                        if filtered_user not in filtered_users:
                            filtered_users.append(filtered_user)

                sentiment = analyze_sentiment(index['text'])
                filtered_post.update(sentiment)
                filtered_posts.append(filtered_post)

    # Prepare the response with the filtered posts
    response = {
        'data': filtered_posts,
        'meta': {
            'newest_id': str(filtered_posts[0]['id']) if filtered_posts and 'id' in filtered_posts[0] else None,
            'oldest_id': str(filtered_posts[-1]['id']) if filtered_posts and 'id' in filtered_posts[-1] else None,
            'result_count': len(filtered_posts)
        }
    }

    # Include 'user' data in the response if 'user.fields' is specified in the arguments
    if user_fields[0]:
        response['includes'] = {'users': filtered_users}

    # Store results in the database
    store_results_in_db(filtered_posts, filtered_users)

    return response

def store_results_in_db(posts, users):
    db_name = getenv('DB_NAME')
    users_dict = {user['id']: user for user in users}  # Convert the list of users to a dictionary
    for post in posts:
        user = users_dict.get(post['author_id'])  # Access the user using the 'author_id' key
        insert_post(db_name, post, user)

if __name__ == '__main__':
    initialize_server()

