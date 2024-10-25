from App.database import db 

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(20), nullable=False)
    description =  db.Column(db.String(20), nullable=False)
    start = db.Column(db.Date, nullable=False)
    end =  db.Column(db.Date, nullable=False, unique=True)
    #Foreign Key(s) 
    creator = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    #Relationship field
    students = db.relationship('Student', secondary='Results', backref='competition', lazy=True)


    def __repr__(self):
        return f'<Competition {self.title}>'

    """ # Creating a new competition with a specific date
    new_competition = Competition(name='Code Challenge', date=date(2024, 10, 25))

    # Adding and committing to the database
    db.session.add(new_competition)
    db.session.commit() """