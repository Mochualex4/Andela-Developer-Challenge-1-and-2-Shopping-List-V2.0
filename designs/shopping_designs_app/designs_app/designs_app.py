import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) 
app.config.from_object(__name__) 

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/signup')
def register():

    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("dashboard.html")

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return render_template('login.html')
    