#USERS/MODELS

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from application import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(128))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.username}'

