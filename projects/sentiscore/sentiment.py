# sentiment.py

from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if 'posts' not in data or not isinstance(data['posts'], list) or len(data['posts']) != 20:
        return jsonify({'error': 'Please provide a list of exactly 20 Twitter posts.'}), 400

    results = []
    for post in data['posts']:
        if not isinstance(post, str):
            return jsonify({'error': 'All posts must be strings.'}), 400
        result = analyze_sentiment(post)
        results.append(result)

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
