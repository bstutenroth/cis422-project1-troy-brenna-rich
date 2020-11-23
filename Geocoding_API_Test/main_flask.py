# main_flask.py
# Brenna Stutenroth
'''
Author: Brenna Stutenroth

uses flask and monogdb
'''
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, request, jsonify, session
from pymongo import MongoClient
import urllib
import json
from werkzeug.utils import secure_filename
from reverse_geocoding_test import *
from routing_main import *
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
#routes to the main page
@app.route('/')
def index():
    #if logged in go to index otherwise go to landing
    if 'username' in session:
        return render_template('index.html')
    else:
        return render_template('landing.html')
#when you view your profile, displays all stores routes
def alreadyStored(route_name):
    users = mongo.db.users
    for key in users.find():
        str_key = str(key)
        for i in key:
            if(i == route_name):
                author = key.get(i, {}).get('author', 'NA')
                if(author == session['username']):
                    return True
    return False


@app.route('/profile')
def profile():
    users = mongo.db.users
    names = []
    li = []
    #get all route dictionaries that are belong to the user signed in
    for key in users.find():
        str_key = str(key)
        for i in key:
            try:
                author = key.get(i, {}).get('author', 'NA')
                addresses = key.get(i, {}).get('adresses', 'NA')
                profile = key.get(i, {}).get('profile', 'NA')
                city = key.get(i, {}).get('city', 'NA')
                precipitation = key.get(i, {}).get('precipitation', 'NA')
                detailed_precipitation = key.get(i, {}).get('detailed_precipitation', 'NA')
                temperature = key.get(i, {}).get('temperature', 'NA')
                humidity = key.get(i, {}).get('humidity', 'NA')
                wind_speed = key.get(i, {}).get('wind_speed', 'NA')
                wind_direction = key.get(i, {}).get('wind_direction', 'NA')
                quality = key.get(i, {}).get('quality', 'NA')
                average_aqi = key.get(i, {}).get('average_aqi', 'NA')
                if(author == session['username']):
                    li.append(key)
                    names.append(i)
            except AttributeError:
                # counters is not a dictionary, ignore and move on
                pass
            #li.append(key.get(i, {}).get('author', 'NA'))
    return render_template('profile.html', names = names)

@app.route('/feed')
def feed():
    users = mongo.db.users
    names = []
    li = []
    #get all route dictionaries that are belong to the user signed in
    for key in users.find():
        str_key = str(key)
        for i in key:
            try:
                author = key.get(i, {}).get('author', 'NA')
                addresses = key.get(i, {}).get('adresses', 'NA')
                profile = key.get(i, {}).get('profile', 'NA')
                public = key.get(i, {}).get('public', 'NA')
                city = key.get(i, {}).get('city', 'NA')
                precipitation = key.get(i, {}).get('precipitation', 'NA')
                detailed_precipitation = key.get(i, {}).get('detailed_precipitation', 'NA')
                temperature = key.get(i, {}).get('temperature', 'NA')
                humidity = key.get(i, {}).get('humidity', 'NA')
                wind_speed = key.get(i, {}).get('wind_speed', 'NA')
                wind_direction = key.get(i, {}).get('wind_direction', 'NA')
                quality = key.get(i, {}).get('quality', 'NA')
                average_aqi = key.get(i, {}).get('average_aqi', 'NA')
                if(public == 'on'):
                    names.append(i)
            except AttributeError:
                # counters is not a dictionary, ignore and move on
                pass
            #li.append(key.get(i, {}).get('author', 'NA'))
    return render_template('feed.html', names = names)
#this re-opens stored files and displays the data
@app.route('/revisit/<div_key>')
def revisit(div_key):
    users = mongo.db.users
    #get the correct dictionary
    for key in users.find():
        str_key = str(key)
        for i in key:
            if(i == div_key):
                try:
                    #get all the info in the dict
                    author = key.get(i, {}).get('author', 'NA')
                    addresses = key.get(i, {}).get('adresses', 'NA')
                    profile = key.get(i, {}).get('profile', 'NA')
                    city = key.get(i, {}).get('city', 'NA')
                    precipitation = key.get(i, {}).get('precipitation', 'NA')
                    detailed_precipitation = key.get(i, {}).get('detailed_precipitation', 'NA')
                    temperature = key.get(i, {}).get('temperature', 'NA')
                    humidity = key.get(i, {}).get('humidity', 'NA')
                    wind_speed = key.get(i, {}).get('wind_speed', 'NA')
                    wind_direction = key.get(i, {}).get('wind_direction', 'NA')
                    quality = key.get(i, {}).get('quality', 'NA')
                    average_aqi = key.get(i, {}).get('average_aqi', 'NA')
                    #display stored info on revisit.html
                    return render_template('revisit.html', profile = profile, adresses = addresses, city = city, precipitation = precipitation,
                        detailed_precipitation = detailed_precipitation, temperature = str(temperature), humidity = str(humidity),
                        wind_speed = str(wind_speed), wind_direction = str(wind_direction), quality = quality, average_aqi = average_aqi)
                except AttributeError:
                    # counters is not a dictionary, ignore and move on
                    pass
#landing page for if a user doesn't have an accout/isnt logged in
@app.route('/landing')
def landing():
    return render_template('landing.html')
#displays routes
@app.route('/display')
def display():
    return render_template('display.html')
#allows only gpx files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#upload gpx file
@app.route('/upload_file', methods=['GET', 'POST'])
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
            filename = secure_filename(file.filename)
            return render_template('display.html', adresses = main(filename))
    return
#gets route info off of start and end point
@app.route('/plan_route', methods=['GET', 'POST'])
def plan_route():
    if request.method == 'POST':
        users = mongo.db.users
        #gets all data for route
        start = request.form['start']
        dest = request.form['end']
        profile = request.form['profile']
        public = request.form.get('public')
        coords = route_main(start, dest)
        route = getRoute(coords,profile)
        forecast = getWeather(coords)
        aqi_pair = getAQI(coords)
        city = forecast["name"]
        precipitation = forecast["weather"][0]["main"]
        detailed_precipitation = forecast["weather"][0]["description"]
        temperature = forecast["main"]["temp"]
        humidity = forecast["main"]["humidity"]
        wind_speed = forecast["wind"]["speed"]
        wind_direction = forecast["wind"]["deg"]
        origin_aqi = aqi_pair[0]["data"]["aqi"]
        destination_aqi = aqi_pair[1]["data"]["aqi"]
        average_aqi = (origin_aqi + destination_aqi) // 2

        if average_aqi <= 50:
            quality = "Good"
        elif average_aqi <= 100:
            quality = "Moderate"
        elif average_aqi <= 150:
            quality = "Unhealthy for Sensitive Groups"
        elif average_aqi <= 200:
            quality = "Unhealthy"
        elif average_aqi <= 300:
            quality = "Very Unhealthy"
        elif average_aqi <= 500:
            quality = "Hazerdous"
        else:
            quality = "Extremely Hazerdous"
        #if this already exists in the database, just display but don't add again
        if(alreadyStored(request.form['route_name'])):
            return render_template('display.html', profile = profile, adresses = printRoute(route), city = city, precipitation = precipitation,
                detailed_precipitation = detailed_precipitation, temperature = str(temperature), humidity = str(humidity),
                wind_speed = str(wind_speed), wind_direction = str(wind_direction), quality = quality, average_aqi = average_aqi)
        else:
            #insert the dictionary for the route into the database and display info
            users.insert({request.form['route_name'] : {
            'author' : session['username'],
            "adresses" : printRoute(route),
            "profile" : profile,
            "public" : public,
            "city" : city,
            "precipitation" : precipitation,
            "detailed_precipitation" : detailed_precipitation,
            "temperature" : str(temperature),
            "humidity" : str(humidity),
            "wind_speed" : str(wind_speed),
            "wind_direction" : str(wind_direction),
            "quality" : quality,
            "average_aqi" : average_aqi}})
            return render_template('display.html', profile = profile, adresses = printRoute(route), city = city, precipitation = precipitation,
            detailed_precipitation = detailed_precipitation, temperature = str(temperature), humidity = str(humidity),
            wind_speed = str(wind_speed), wind_direction = str(wind_direction), quality = quality, average_aqi = average_aqi)
    return render_template('display.html')

#login function
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username/password combination'

#register user
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        #if user doesn't already exist add to database
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            #users.insert({session['username']+"_routes" : {}})
            return redirect(url_for('index'))
        return 'That username already exists!'

    return render_template('register.html')
#logout function
@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('username', None)
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
if app.debug:
    app.logger.setLevel(logging.DEBUG)
