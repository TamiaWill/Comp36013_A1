from App.database import db 

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score =  db.Column(db.Float, nullable=False)
    rank =  db.Column(db.Integer, nullable=False)
    start = db.Column(db.Date, nullable=False)
    end =  db.Column(db.Date, nullable=False)
    #Foreign keys
    competitionID = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self):
        return f'<Result {self.title}>'


    #Relationship fields
    # A relationship field allows you to access all the results of a competition directly, 
    # like a list of Result objects. So instead of handling numbers (IDs), 
    # you can handle full objects
    # A relationship defines how SQLAlchemy (or another ORM) should handle the association between models. 
    # It can represent different types of relationships, such as one-to-many, many-to-one, and many-to-many.