# CUSTOMERS/FORMS

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired, Required
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

from customers.models import Customer

class CustomerForm(FlaskForm):
    customer_name = StringField('Customer Name', validators=[InputRequired(),Length(max=100)])
    submit = SubmitField('Register Customer')


    def check_customer(self,field):
        if Customer.query.filter_by(customer_name=field.data).first():
            raise ValidationError (f'User {field.data} is already registered')