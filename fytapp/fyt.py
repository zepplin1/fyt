from fytapp import app
from flask import Flask, render_template
from db import get_db

@app.route('/')
def index():
	return 'homepage'

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def reg():
	return render_template('reg.html')
