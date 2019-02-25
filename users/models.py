from application import db


from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(25))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.username}'

