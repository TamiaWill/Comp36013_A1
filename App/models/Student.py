from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname =  db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    #Relationship fields
    results = db.relationship('Result', secondary='Student' backref='student', lazy=True)
    

    def __init__(self, username, password, email, user_type):
        self.username = username
        self.set_password(password)
        self.email = email
        self.user_type = user_type


    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

