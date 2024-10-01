from App.database import db
from .user import User

class Admin(User):
    adminID = db.Column(db.Integer, db.ForeignKey('users.userID'), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    # Relationship to competitions created by admin
    competitions = db.relationship('Competition', backref='creator', lazy=True)

    def __init__(self, username, email, password, name):
        super().__init__(username, email, password, user_type='admin')
        self.name = name