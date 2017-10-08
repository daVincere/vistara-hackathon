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

app.config['MONGO_DBNAME'] = 'vistara'
app.config['MONGO_URI'] = 'mongodb://user1:user1@ds113785.mlab.com:13785/vistara'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', data='test')

@app.route('/dashboard')
def dashboard():
	#present users to day
	analytics = []

	userdata = {'Monday' : 2500, 'Tuesday' : 2100, 'Wednesday' : 3250, 'Thursday': 1900, 'Friday' : 2300, 'Saturday' : 4320, 'Sunday' : 5100}
	route = {'from' : 'Delhi', 'to' : 'Mumbai', 'userdata' : userdata}

	analytics.append(route)

	return render_template('dashboard.html', analytics=analytics)

@app.route('/postfromapp', methods=['POST'])
def post_from_app():
	if request.method == "POST":
		formdata = (request.get_json())

		#parse karna h isse
		username = formdata['username']
		route = formdata['route']
		date = formdata['date']
		price = formdata['price']
		choice = formdata['choice']
		score = formdata['score']

		#leaderboard me add kar
		usersdata = mongo.db.usersdata
		data = usersdata.find_one({'maindata' : 'maindata'})

		temp = {}
		flag = 0

		for item in data['data']:
			if(item['username'] == username):
				flag = 1
				_history = []

				#append
				_history = item['history']
				h = [{"date" : date, "score" : score},]
				_history.extend(h)

				result = mongo.db.usersdata.update_one({"username" : item['username']}, {'$set' : {"username" : "lodu"}})

		if(flag == 0):
			#create
			new_user = {}

			new_user['username'] = formdata['username']
			new_user['route'] = formdata['route']

			history = []
			h = {}
			h['date'] = formdata['date']
			h['price'] = formdata['price']
			history.append(h)

			new_user['choice'] = formdata['choice']
			new_user['score'] = formdata['score']
			new_user['history'] = history

			data['data'].append(new_user)

			result = mongo.db.usersdata.update_one({"maindata" : 'maindata'}, {'$set' : {"data" : data}})

			return(jsonify(data['data']))

		usersdata = mongo.db.usersdata
		existing_user = usersdata.find_one({'username' : formdata['username']})

		history = []

		h = {"date" : date, "score" : score}
		history.append(h)

		result = mongo.db.usersdata.update_one({"username" : formdata['username']}, {'$set' : {"history" : history}})

		print(result)

		return ("GG")

@app.route('/usersdata')
def get_usersdata():
	usersdata = mongo.db.usersdata

	data = usersdata.find_one({'maindata' : 'maindata'})

	leaderboard = []
	for item in data['data']:
		person = {}
		person['username'] = item['username']
		person['score'] = item['score']

		leaderboard.append(person)

	print(leaderboard)



	return ("GG")

def get_leaderboard(data):

	return (leaderboard)

			# users.insert({'name' : request.form['username'], 'password' : hashpass})
			# session['username'] = request.form['username']
			# return redirect(url_for('changes'))

		#user rank return karni h





	


'''

'''

if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True)