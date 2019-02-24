from flask import Flask, Blueprint

from customers.models import Customer

customer_bp = Blueprint('customer_bp', __name__)