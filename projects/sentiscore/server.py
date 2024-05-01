# server.py
import sys
from flask import Flask, render_template
from database import check_database_exists

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def initialize_server():
    if check_database_exists():
        app.run()
    else:
        print("Database 'sentiscore' does not exist.")
        sys.exit()

if __name__ == '__main__':
    initialize_server()
