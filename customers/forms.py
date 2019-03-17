# CUSTOMERS/FORMS

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired, Required
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

from customers.models import Customer

class CustomerForm(FlaskForm):
    name = StringField('Customer Name', validators=[InputRequired(),Length(max=100)])
    submit = SubmitField('Register Customer')

    #########################
    ### CUSTOM VALIDATORS ###
    #########################

    def validate_name(self,name):
        # Checkif name already in the database 
        customer = Customer.query.filter_by(name=name.data).first()
        if customer is not None:
            raise ValidationError ('Customer already exists')