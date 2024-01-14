from flask import Flask, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import bcrypt

app = Flask(__name__)

# Database connection setup
engine = create_engine(os.getenv("postgresql://postgres:2Cc-ebBefcfe1aD*Ag4-4GEF52Faa63B@postgres.railway.internal:5432/railway"))
db = scoped_session(sessionmaker(bind=engine))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')  # Ensure password is in bytes

        # Query to retrieve the user's stored hash
        user = db.execute('SELECT password_hash FROM customer WHERE username = :username', {"username": username}).fetchone()

        if user and bcrypt.checkpw(password, user.password_hash.encode('utf-8')):
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
