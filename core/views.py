from flask import Flask, Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return 'Hello There'