from flask import Flask, request, redirect
import psycopg2
import os
from config import access_cred
import bcrypt
from cryptography.fernet import Fernet

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    return conn
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')  # Ensure password is in bytes

        # Connect to the DB
        conn = get_db_connection()
        cur = conn.cursor()

        # Query to retrieve the user's stored hash
        cur.execute('SELECT password_hash FROM customer WHERE username = %s', (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and bcrypt.checkpw(password, user[0].encode('utf-8')):  # Check the provided password against the stored hash
            return redirect('https://tonyarkaysia.github.io/isl-profile')
        else:
            return redirect('https://tonyarkaysia.github.io/isl-retry-login')

    return redirect('https://tonyarkaysia.github.io/isl-retry-login')

@app.route('/add-api-key', methods=['POST'])
def add_api_key():

    apikey = request.form['apikey']

    if apikey == "w-f_JoRyjxgqJKasc6glAQNFqFJIUGE7HwF_Lo0fQEA":  # Replace with real validation
        return redirect('https://tonyarkaysia.github.io/isl-cybergateway')
    else:
        return redirect('https://tonyarkaysia.github.io/isl-retry-login')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))




