# server.py
from flask import Flask, render_template
from database import check_database_exists, create_database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def initialize_server():
    if check_database_exists():
        app.run()
    else:
        print("Database 'sentiscore' does not exist.")
        print("Creating 'sentiscore' database.")
        create_database()

if __name__ == '__main__':
    initialize_server()
