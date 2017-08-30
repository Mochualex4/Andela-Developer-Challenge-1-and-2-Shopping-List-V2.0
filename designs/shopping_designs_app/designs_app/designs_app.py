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

    return render_template("dashboard.html")

@app.route('/login')
def login():
    
    return render_template("login.html")
