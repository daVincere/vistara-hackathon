from flask import Flask, render_template, request, url_for, jsonify, make_response, session, redirect
from functools import wraps
import pyrebase
import cloudinary
import json
import cloudinary.uploader
from time import time
from random import random
import milestones as mls
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

cloudinary.config(
  cloud_name = 'dglr3rxzz',  
  api_key = '463868796246575',  
  api_secret = 'YrBObQMCG_Ulo6dfdRfoQG-uCCM'  
)

firebase = pyrebase.initialize_app(config)
firebase_auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, static_url_path='/static')

app.config['MONGO_DBNAME'] = 'abidbgac'
app.config['MONGO_URI'] = 'mongodb://user1:abcd1234@ds159493.mlab.com:59493/abidbgac'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', data='test')


if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True)