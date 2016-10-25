from fytapp import app
from flask import Flask

@app.route('/')
def index():
	return 'this is a test'

@app.route('/login')
def login():
	return 'this is the login page'
