from App.database import db
from .user import User

class Student(User):
    studentID = db.Column(db.Integer, db.ForeignKey('users.userID'), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    major = db.Column(db.String(50), nullable=False)

    results = db.relationship('Result', backref='student', lazy=True)

    def __init__(self, username, password, email, name, year, major):
        super().__init__(self, username, password, email, user_type='student')
        self.name = name
        self.year = year
        self.major = major