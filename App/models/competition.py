from App.database import db

class Competition (db.Model):
    competitionID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    start = db.Column(db.Date, nullable=False)
    end = db.Column(db.Date, nullable=False)
    # Relationship with Result
    results = db.relationship('Result', backref='competition', lazy=True)
    # Foreign key: competition to Admin
    adminID = db.Column(db.Integer, db.ForeignKey('admins.userID'), nullable=False)

    def __init__(self, title, description, start, end):
        self.title = title
        self.description = description
        self.start = start
        self.end = end