import json

from flask import Flask, jsonify, request

app = Flask(__name__)

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Predefined dictionary with acceptable keys and values
acceptable_args = {
    'ids': ['1667982248614730000'],
    'tweet.fields': ['author_id', 'created_at', 'id', 'text'],
    'user.fields': ['created_at', 'description', 'id', 'name', 'username']
}

@app.route('/posts', methods=['GET'])
def get_posts():
    # Get request arguments
    args = request.args.to_dict()

    # Validate request arguments
    errors = []
    for key, string in args.items():
        values = string.split(',')
        if key not in acceptable_args or not isinstance(acceptable_args[key], list):
            errors.append(f"Invalid argument: {key}")
            continue  # Skip further checks for this key since it's already invalid
        for value in values:
            if value not in acceptable_args[key]:
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

    return tweet_fields + user_fields

"""     # Filter data based on request arguments
    posts = load_json('posts.json')
    filtered_posts = []
    for post in posts['data']:
        match = True
        for key, string in args.items():
            values = string.split(',')
            if key in post and str(post[key]) not in values:
                match = False
                break
            if match:
                filtered_posts.append(post) """

    #return 'The request arguments were successful.'

    #return jsonify(load_json('posts.json'))

    # Prepare the response
"""     response = {
        'data': filtered_posts,
        'meta': {
            'result_count': len(filtered_posts)
        }
    }

    return jsonify(response) """

if __name__ == '__main__':
    app.run(debug=True)
