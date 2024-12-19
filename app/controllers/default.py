from app import app
from flask import render_template
from markupsafe import escape

@app.route('/index')
@app.route('/')
def index():
    return 'Index page'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return 'About Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

