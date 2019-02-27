from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.valdators import DataRequired, Email, EqualTo, Length, InputRequired, Required
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

from users.models import User

##############################
######## REGISTER ############
##############################

class RegisterForm(FlaskForm):
    username = StringField('Name',validators=[InputRequired()])
    email = StringField('Email',
            validators=[InputRequired('Please enter your email address'),
                        Email()])
    password = PasswordField('Password',
                validators=[InputRequired('Please enter a password'),
                            Length(min=6,max=25)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[InputRequired('Confirm password'),
                        EqualTo('password', message = 'Passwords must match')])
    submit = SubmitField('Register')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError (f'User {field.data} is already registered')
    
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError (f'User with email {field.data} has already registered')
        





##############################
########## LOGIN #############
##############################


##############################
######### UPDATE #############
##############################