from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Result(db.Model):
    __tablename__ = 'results'
    
    resultID = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer)
    score = db.Column(db.Float)
    # Foreign keys: Student and Competition
    studentID = db.Column(db.Integer, db.ForeignKey('students.studentID'), nullable=False)
    competitionID = db.Column(db.Integer, db.ForeignKey('competitions.competitionID'), nullable=False)

    def __init__(self, position, score, studentID, competitionID):
        self.position = position
        self.score = score
        self.studentID = studentID
        self.competitionID = competitionID