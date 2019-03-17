# USERS/VIEWS.PY
from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from users.models import User
from application import login_manager, db
from users.forms import RegisterForm, LoginForm

user_bp = Blueprint('user_bp',__name__)

#####################

###### REGSTER ######
#####################

@user_bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Create hashed password
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # database submission
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering, now please log in')
        return redirect(url_for('.login'))
       
    return render_template('users/register.html', form=form)
    
####################
###### LOGIN #######
####################

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                #flash('Login successful')
           # if user has been redirected from another page 
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core_bp.index')
                return redirect(next)
    return render_template('users/login.html', form=form)

####################
###### LOGOUT ######
####################
@user_bp.route('/logout')

def logout():
    logout_user()
    flash('You are now logged out')
    return redirect(url_for('.login'))

####################
###### DELETE ######
####################