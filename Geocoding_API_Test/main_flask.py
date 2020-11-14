# main_flask.py
# Brenna Stutenroth

import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, request, jsonify, session
from pymongo import MongoClient
import urllib
import json
from werkzeug.utils import secure_filename
from reverse_geocoding_test import *
import logging
from bson.json_util import dumps
import bcrypt
import config

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'gpx'}

app = Flask(__name__)
CONFIG = config.configuration()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'some secret key'
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
mongo = client.db


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return render_template('landing.html')

@app.route('/get_route')
def get_route():
    return render_template('get_route.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/loginform')
def loginform():
    return render_template('loginform.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/get_route', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #run main() in reverse_geocoding_test and return results on display.html
            filename = secure_filename(file.filename)
            return render_template('display.html', adresses = main(filename))
    return


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('username', None)
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
if app.debug:
    app.logger.setLevel(logging.DEBUG)
