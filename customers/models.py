from application import db

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f'Customer: {self.name}'