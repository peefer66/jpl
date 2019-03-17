from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required
from application import db

from customers.forms import CustomerForm
from customers.models import Customer

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/new_customer', methods=['GET','POST'])
@login_required
def new_customer():
    form=CustomerForm()
    
    if form.validate_on_submit():
        customer = Customer(name=form.name.data)
        db.session.add(customer)
        db.session.commit()
        flash('Customer Record Created')
        return redirect(url_for('core_bp.index'))
         
    return render_template('/customers/register.html', form=form)
