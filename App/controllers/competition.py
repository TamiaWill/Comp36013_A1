""" from App.models import Competition, Result, User
from App.database import db


def create_competition(admin_id, title, description, start, end):
    # Check if the user is an admin
    admin = User.query.get(admin_id)
    if not admin or admin.role != 'admin':
        return {"message": "Only admins can create competitions."}
    
    new_competition = Competition(title=title, description=description, start=start, end=end, adminID=admin_id)
    db.session.add(new_competition)
    db.session.commit()
    return new_competition

def get_competition(competition_id):
    return Competition.query.get(competition_id)

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()
    if not competitions:
        return []
    return [competition.get_json() for competition in competitions]

def update_competition(competition_id, title=None, description=None, start=None, end=None):
    competition = get_competition(competition_id)
    if not competition:
        return {"message": "Competition not found."}

    if title:
        competition.title = title
    if description:
        competition.description = description
    if start:
        competition.start = start
    if end:
        competition.end = end

    db.session.commit()
    return competition

def delete_competition(competition_id):
    competition = get_competition(competition_id)
    if not competition:
        return {"message": "Competition not found."}

    db.session.delete(competition)
    db.session.commit()
    return {"message": "Competition deleted successfully."} """