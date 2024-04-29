import psycopg
from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)

def db_connection():
    conn = psycopg.connect(host=getenv('DB_HOSTNAME'),
                           dbname=getenv('DB_NAME'),
                           user=getenv('DB_USERNAME'),
                           password=getenv('DB_PASSWORD'))
    return conn

@app.route('/')
def index():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sentiscore;')
    sentiscore = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', sentiscore=sentiscore)

if __name__ == '__main__':
    app.run()
