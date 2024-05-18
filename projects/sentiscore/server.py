import logging, json
from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from textblob import TextBlob
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
    app.run(debug=True)


# Load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Predefined dictionary with acceptable keys and values
# The keys are the acceptable arguments that can be passed in the request
# The values are either a list of acceptable values or a function that validates the argument value
acceptable_args = {
    'ids': lambda x: x.isdigit() and len(x) == 19,
    'tweet.fields': ['author_id', 'created_at', 'id', 'text'],
    'user.fields': ['created_at', 'description', 'id', 'name', 'username']
}

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
    posts = load_json('posts.json')
    filtered_posts = []
    filtered_users = []
    if 'ids' in args:
        ids = args['ids'].split(',')
        ids = [int(id) for id in ids]
        for post in posts['data']:
            if post['id'] in ids:
                # Include the specified tweet fields (if requested in the arguments)
                filtered_post = {key: post[key] for key in tweet_fields if key in post} if tweet_fields else post

                # Include the specified user fields (if requested in the arguments)
                author_id = post['author_id']
                for user in posts['includes']['users']:
                    if user['id'] == author_id:
                        filtered_user = {key: user[key] for key in user_fields if key in user} if user_fields else user
                        if filtered_user not in filtered_users:
                            filtered_users.append(filtered_user)

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

    return response

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

# Retrieve data and perform sentiment analysis (pretend to get the data from an api service)
with app.test_client() as client:
    response = client.get('/tweets?ids=1668031228811800000,1668029197065800000,1668017215944130000,1668014822326140000,1668013802359490000,1668013122567780000,1668012189955810000,1668011771532040000,1668011185248120000,1668009508633750000,1668008743328510000,1668006873604280000,1668006548335930000,1668005894326480000,1668004568637080000,1668003032259260000,1667999474684390000,1667996790036000000,1667992787885620000,1667982248614730000&tweet.fields=id,created_at,author_id,text&user.fields=id,name,username,description')

    # Perform sentiment analysis on each post
    data = response.json  # Access the 'data' key directly from the response.json dictionary
    for post in data:
        text = post['text']
        sentiment = analyze_sentiment(text)
        post['sentiment'] = sentiment

    # Print the modified response
    print(response.json)

if __name__ == '__main__':
    initialize_server()

