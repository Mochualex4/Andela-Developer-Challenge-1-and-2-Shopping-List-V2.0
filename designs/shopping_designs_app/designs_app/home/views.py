from flask import abort, render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
def homepage():
    
    return render_template('home/index.html', title="Shop List")

@home.route('/dashboard')
#make user login first
def dashboard():
    
    return render_template('home/dashboard.html', title="Dashboard")


