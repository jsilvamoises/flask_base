from flask import Flask, flash, redirect, request, url_for
from flask.templating import render_template
from werkzeug.urls import url_parse


from app.auth.forms import LoginForm, RegistrationForm
from app.models.models import User
from flask_login import current_user, login_required, login_user, logout_user
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():       
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash(f'Inválid username or password','error')            
            return redirect(url_for('auth.login')) 
        else:
            login_user(user,remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.index')
            flash(f'Bem Vindo!!','success')   
            return redirect(next_page)
    return render_template('login/login.html',form=form,title='Login')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data,email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulation you are now a registred user','success')
            return redirect(url_for('auth.login'))
        except Exception as erro:
            flash(f'Error: {erro}','error')
            redirect(url_for('auth.register'))  


    return render_template('login/register.html',form=form,title='Register')

@login_required
@auth.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user,'body':'body 1'},
        {'author':user,'body':'body 2'}
    ]
    return render_template('user.html',user=user,posts=posts)



@auth.route("/starter")
def starter():
    return render_template('fragments/starter.html')