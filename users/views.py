from flask import Flask, Blueprint

from users.models import User

user_bp = Blueprint('user_bp',__name__)