# USERS/VIEWS.PY
from flask import Flask, Blueprint, render_template


from users.models import User
from application import login_manager
from users.forms import RegisterForm

user_bp = Blueprint('user_bp',__name__)

###### REGSTER ######
@user_bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

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
