""" from App.models import Student, User, Competition, Result
from App.database import db

def create_student(username, password, name, year, major):
    new_student = Student(username=username, password=password, name=name, year=year, major=major)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_student_by_username(username):
    return User.query.filter_by(username=username, role='student').first()

def get_student(id):
    return User.query.get(id)

def get_all_students():
    return User.query.filter_by(role='student').all()

def get_all_students_json():
    students = User.query.filter_by(role='student').all()
    if not students:
        return []
    return [student.get_json() for student in students]

def update_student(id, username=None, email=None, password=None):
    student = get_student(id)
    if student and student.role == 'student':
        if username:
            student.username = username
        if email:
            student.email = email
        if password:
            student.set_password(password) 
        
        db.session.commit()
        return student
    return None

def delete_student(id):
    student = get_student(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return {"message": f"Student {id} successfully deleted."}
    return None


# View all competitions
def view_competitions():
    competitions = Competition.query.all()
    return [competition.get_json() for competition in competitions]

# View competition results
def view_competition_results(competition_id):
    results = Result.query.filter_by(competition_id=competition_id).all()
    if not results:
        return {"message": "No results found for this competition."}
    return [result.get_json() for result in results]

# Student participates in a competition
def participate_in_competition(student_id, competition_id):
    student = get_student(student_id)
    competition = Competition.query.get(competition_id)

    if student and competition:
        # Create a new participation or result entry (depends on your logic)
        new_result = Result(student_id=student_id, competition_id=competition_id)
        db.session.add(new_result)
        db.session.commit()
        return {"message": f"Student {student_id} successfully registered for competition {competition_id}."}
    
    return {"message": "Student or competition not found."} """