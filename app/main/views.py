from flask import Flask, flash, redirect, request, url_for
from flask.templating import render_template
from werkzeug.urls import url_parse


from app.auth.forms import LoginForm, RegistrationForm
from app.models.models import User
from flask_login import current_user, login_required, login_user, logout_user
from . import main


@main.route('/')
@main.route('/home')
@main.route('/index')
@login_required
def index():
    
    
    posts = [
        {'Author':'Moises Silva','body':'Corpo 1'},
        {'Author':'Simão Pedro','body':'Corpo 2'},
    ]
    return render_template('index.html',title='Home',posts=posts)
