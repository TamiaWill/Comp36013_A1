from App.database import db
from .user import User

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname =  db.Column(db.String(20), nullable=False, unique=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    major = db.Column(db.String(50), nullable=False)

    results = db.relationship('Result', backref='student', lazy=True)

    def __init__(self, fname, lname, email, year, major):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.year = year
        self.major = major