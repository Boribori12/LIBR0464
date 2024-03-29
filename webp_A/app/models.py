from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    store_name = db.Column(db.String(200), nullable = False)
    rate = db.Column(db.Integer, nullable = False)
    desc = db.Column(db.Text(), nullable = False)
    img = db.Column(db.BLOB(), nullable = False)
    location = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref = db.backref('item_set'))
    modify_date = db.Column(db.DateTime(), nullable = True)