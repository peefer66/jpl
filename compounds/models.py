from datetime import datetime

from application import db

class Compound(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cpd_no = db.Column(db.String(25),unique=True)
    comments = db.Column(db.String(255))
    date_issued = db.Column(db.DateTime)

    def __init__(self,cpd_no,comments,date_issued):
        self.cpd_no = cpd_no
        self.comments = comments
        self.date_issued = date_issued
    def __retr__(self):
        return f'Compound Number: {self.cpd_no}'
