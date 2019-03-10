#CORE/VIEWS.PY

from flask import Flask, Blueprint
from flask_login import login_required

core_bp = Blueprint('core_bp',__name__)

@core_bp.route('/')
@login_required
def index():
    return 'Hello There'