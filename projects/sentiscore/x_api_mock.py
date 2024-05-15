import json

from flask import jsonify, request


def load_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {filename} is not a valid JSON file.")
        return None

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
    query_params = {field: [f for f in request_args.get(field, default = '', type = str).split(',') if f and f in valid_field] for field, valid_field in valid_fields.items()}
    return query_params

def check_fields(request_args, valid_fields):
    errors = [f"Invalid {field} value(s) provided." for field, valid_field in valid_fields.items() if not all(f in valid_field for f in request_args.get(field, default = '', type = str).split(',') if f)]
    return errors[0] if errors else None

def get_posts():
    # Load replicate api data
    posts = load_json('posts.json')

    # Get the 'ids" query parameter from request
    ids_param = request.args.get('ids', default = '1', type = str)

    # Split the parameter into a list of IDs
    ids = set(int(id) for id in ids_param.split(','))

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
    requested_fields = {field: define_query_params(request.args, {field: valid_field}).get(field, []) for field, valid_field in valid_fields.items()}
    error = check_fields(request.args, valid_fields)
    if error:
        return jsonify({"error": error}), 400

    # Find the posts with the given IDs
    responses = []
    for post in posts['data']:
        if int(post['id']) in ids:
            # Create a response for each post
            response = {'data': {}, 'includes': {}}

            # Add tweet.fields to the response
            for field in requested_fields.get('tweet.fields', []):
                if field in post:
                    response['data'][field] = post[field]

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
                    response['data'][expansion] = current

            # Add additional fields to the response
            includes = posts.get('includes', {})
            if 'media' in includes and 'attachments.media_keys' in valid_expansions:
                response['includes']['media'] = [{field: media[field] for field in media if field in requested_fields['media.fields']} for media in includes['media']]

            if 'places' in includes and 'geo.place_id' in valid_expansions:
                response['includes']['places'] = [{field: place[field] for field in place if field in requested_fields['place.fields']} for place in includes['places']]

            if 'polls' in includes and 'attachments.poll_ids' in valid_expansions:
                response['includes']['polls'] = [{field: poll[field] for field in poll if field in requested_fields['poll.fields']} for poll in includes['polls']]

            if 'users' in includes and 'author_id' in valid_expansions and 'author_id' in requested_fields['expansions']:
                user = next((user for user in includes['users'] if str(user['id']) == str(post['author_id'])), None)
                if user:
                    response['includes']['users'] = [{field: user[field] for field in user if field in requested_fields['user.fields']}]

            responses.append(response)

    return jsonify(responses)

def get_post(id):

    # Load replicate api data
    posts = load_json('posts.json')

    # Convert the id to int
    id = int(id)

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
    requested_fields = {field: define_query_params(request.args, {field: valid_field}).get(field, []) for field, valid_field in valid_fields.items()}
    errors = [check_fields(request.args, {field: valid_field}) for field, valid_field in valid_fields.items() if check_fields(request.args, {field: valid_field})]

    if errors:
        return jsonify({"error": errors[0]}), 400

    # Find the post with the given ID
    post = next((post for post in posts['data'] if int(post['id']) == id), None)

    if post:
        # Create a response for the post
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
        includes = posts.get('includes', {})
        if 'media' in includes and 'attachments.media_keys' in valid_expansions:
            response['media'] = [{field: media[field] for field in media if field in requested_fields['media.fields']} for media in includes['media']]

        if 'places' in includes and 'geo.place_id' in valid_expansions:
            response['places'] = [{field: place[field] for field in place if field in requested_fields['place.fields']} for place in includes['places']]

        if 'polls' in includes and 'attachments.poll_ids' in valid_expansions:
            response['polls'] = [{field: poll[field] for field in poll if field in requested_fields['poll.fields']} for poll in includes['polls']]

        if 'users' in includes and 'author_id' in valid_expansions and 'author_id' in requested_fields['expansions']:
            user = next((user for user in includes['users'] if str(user['id']) == str(post['author_id'])), None)
            if user:
                response['author'] = {field: user[field] for field in user if field in requested_fields['user.fields']}

        return jsonify(response)

    return jsonify({"error": "Post not found"}), 404
