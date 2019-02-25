from datetime import datetime

from application import db

#####################################
########### Compound ################
#####################################

class Compound(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    cpd_no = db.Column(db.String(25),unique=True)
    comments = db.Column(db.String(255))
    date_issued = db.Column(db.DateTime)

    category = db.relationship('Category',backref=db.backref('compounds',lazy='dynamic'))
    customer = db.relationship('Customer',backref=db.backref('compounds',lazy='dynamic'))


    def __init__(self,cpd_no,comments,date_issued):
        self.cpd_no = cpd_no
        self.comments = comments
        self.date_issued = date_issued
    def __repr__(self):
        return f'Compound Number: {self.cpd_no}'

######################################
############ Category ################
######################################

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50),unique=True)

    def __init__(self,category):
        self.category = category
    
    def __repr__(self):
        return f'Category: {self.category}'