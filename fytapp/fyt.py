from fytapp import app
from flask import Flask, render_template
from db import get_db

# route http "/" to this
@app.route('/')
def index():
	return 'homepage'

# serve login.html to '/login'
@app.route('/login')
def login():
	return render_template('login.html')

# serve reg.html to '/register'
@app.route('/register')
def reg():
	return render_template('reg.html')
