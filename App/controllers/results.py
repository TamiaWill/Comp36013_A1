from App.models import Result, User, Competition
from App.database import db

def create_result(student_id, competition_id, score):
    # Check if the student exists
    student = User.query.get(student_id)
    if not student or student.role != 'student':
        return {"message": "Only students can have results."}
    
    # Check if the competition exists
    competition = Competition.query.get(competition_id)
    if not competition:
        return {"message": "Competition not found."}

    new_result = Result(student_id=student_id, competition_id=competition_id, score=score)
    db.session.add(new_result)
    db.session.commit()
    return new_result

def get_result(result_id):
    return Result.query.get(result_id)

def get_results_by_student(student_id):
    results = Result.query.filter_by(student_id=student_id).all()
    return results

def get_results_by_competition(competition_id):
    results = Result.query.filter_by(competition_id=competition_id).all()
    return results

def update_result(result_id, score=None):
    result = get_result(result_id)
    if not result:
        return {"message": "Result not found."}
    
    if score is not None:
        result.score = score

    db.session.commit()
    return result

def delete_result(result_id):
    result = get_result(result_id)
    if not result:
        return {"message": "Result not found."}

    db.session.delete(result)
    db.session.commit()
    return {"message": "Result deleted successfully."}
