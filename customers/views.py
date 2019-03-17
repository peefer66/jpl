from flask import Flask, Blueprint, render_template
from flask_login import login_required

from customers.forms import CustomerForm

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/new_customer', methods=['GET','POST'])
@login_required
def new_customer():
    form=CustomerForm()
    return render_template('/customers/register.html', form=form)
