from flask import Flask, Blueprint

from compounds.models import Compound

compound_bp = Blueprint('compound_bp',__name__)