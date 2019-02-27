# USERS/VIEWS.PY
from flask import Flask, Blueprint

from users.models import User
from application import login_manager

user_bp = Blueprint('user_bp',__name__)

###### REGSTER ######
@user_bp.route('/register')
def register():
    return 'Registered'

###### LOGIN #######
@user_bp.route('/login')
def login():
    return 'Login'

###### LOGOUT ######
@user_bp.route('/logout')
def logout():
    return 'Logged Out'

###### DELETE ######
