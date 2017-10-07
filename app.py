from flask import Flask, render_template, request, url_for, jsonify, make_response, session, redirect
from functools import wraps
import json
from time import time
from random import random
from flask_pymongo import PyMongo
import bcrypt
import os

config = {
	"apiKey": "AIzaSyCYx7SRzIaP-w-ueFQ8fgkV69ekzMSqRfM",
	"authDomain": "abidb-dad90.firebaseapp.com",
	"databaseURL": "https://abidb-dad90.firebaseio.com",
	"projectId": "abidb-dad90",
	"storageBucket": "",
	"messagingSenderId": "800861923142"
}

app = Flask(__name__, static_url_path='/static')

app.config['MONGO_DBNAME'] = 'abidbgac'
app.config['MONGO_URI'] = 'mongodb://user1:abcd1234@ds159493.mlab.com:59493/abidbgac'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('base.html', data='test')

@app.route('/dashboard')
def dashboard():
	#present users to day
	analytics = []

	userdata = {'Monday' : 2500, 'Tuesday' : 2100, 'Wednesday' : 3250, 'Thursday': 1900, 'Friday' : 2300, 'Saturday' : 4320, 'Sunday' : 5100}
	route = {'from' : 'Delhi', 'to' : 'Mumbai', 'userdata' : userdata}

	analytics.append(route)

	return render_template('dashboard.html', analytics=analytics)

app.route('/postfromapp', methods=['POST'])
def post_from_app():
	if request.method == "POST":
		formdata = (request.form).to_dict()

		#parse karna h isse
		username = formdata['username']
		route = formdata['route']
		day = formdata['day']
		price = formdata['price']
		choice = formdata['choice']
		score = formdata['score']

		#leaderboard me add kar
		

		#user rank return karni h





	


'''

'''

if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True)