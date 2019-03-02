# USERS/VIEWS.PY
from flask import Flask, Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from users.models import User
from application import login_manager, db
from users.forms import RegisterForm

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
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering')
        
        return redirect(url_for('core_bp.index'))
 
        
    return render_template('users/register.html', form=form)
    

###### LOGIN #######
@user_bp.route('/login')
def login():
    return 'Login'

###### LOGOUT ######
@user_bp.route('/logout')
def logout():
    return 'Logged Out'

###### DELETE ######
