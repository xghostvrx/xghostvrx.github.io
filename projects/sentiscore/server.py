# server.py
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template
from database import check_database_exists, create_database, check_table_exists, create_table

load_dotenv(override=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def initialize_server():
    db_name = getenv('DB_NAME')
    if not check_database_exists(db_name):
        print(f"Database '{db_name}' does not exist.")
        print(f"Creating '{db_name}' database.")
        create_database(db_name)
    elif not check_table_exists(db_name):
        print("'posts' table does not exists.")
        print("Creating 'sentiscore' table.")
        create_table(db_name)
    else:
        print('The app started sucker.')
        # app.run()

if __name__ == '__main__':
    initialize_server()
