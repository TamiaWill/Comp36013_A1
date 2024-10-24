""" from App.models import Admin, User, Competition, Result
from App.database import db
import csv
from flask import request, jsonify

def create_admin(username, email, password):
    new_admin = Admin(username=username, email=email, password=password)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def get_all_admins():
    return User.query.filter_by(role='admin').all()

def get_admin_by_username(username):
    return User.query.filter_by(username=username, role='admin').first()

def update_admin(admin_id, username=None, email=None, password=None):
    admin = User.query.get(admin_id)
    
    if not admin:
        return {"message": "Admin not found."}

    if admin.role != 'admin':
        return {"message": "User is not an admin."}

    if username:
        admin.username = username
    if email:
        admin.email = email
    if password:
        admin.set_password(password)
    
    db.session.add(admin)
    db.session.commit()

    return {"message": f"Admin {admin.username} updated successfully."}


# Create a new competition
def create_competition(admin_id, title, description, start, end):
    admin = Admin.query.get(admin_id)
    if not admin:
        return {"message": "Admin not found."}

    new_competition = Competition(title=title, description=description, start=start, end=end, adminID=admin_id)
    db.session.add(new_competition)
    db.session.commit()

    return {"message": f"Competition '{title}' created successfully.", "competition_id": new_competition.competitionID}

# View all competitions
def view_competitions():
    competitions = Competition.query.all()
    return [competition.get_json() for competition in competitions]

# View competitions created by the admin
def view_admin_competitions(admin_id):
    admin = Admin.query.get(admin_id)
    if not admin:
        return {"message": "Admin not found."}
    
    competitions = Competition.query.filter_by(adminID=admin_id).all()
    return [competition.get_json() for competition in competitions]

# View competition results
def view_competition_results(competition_id):
    competition = Competition.query.get(competition_id)
    if not competition:
        return {"message": "Competition not found."}

    results = Result.query.filter_by(competition_id=competition_id).all()
    if not results:
        return {"message": "No results found for this competition."}

    return [result.get_json() for result in results]

# Delete a competition
def delete_competition(competition_id):
    competition = Competition.query.get(competition_id)
    if not competition:
        return {"message": "Competition not found."}

    # Delete the competition
    db.session.delete(competition)
    db.session.commit()

    return {"message": f"Competition '{competition.title}' deleted successfully."}

# Import results from file
def import_results():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    results = []
    
    if file:
        # Read the CSV file
        csv_file = csv.reader(file.stream)
        for row in csv_file:
            try:
                student_id = int(row[0])
                competition_id = int(row[1])
                score = float(row[2])
                
                # Create a new Result instance
                result = Result(student_id=student_id, competition_id=competition_id, score=score)
                results.append(result)
            except (ValueError, IndexError):
                return jsonify({"message": "Error processing row: {}".format(row)}), 400

        db.session.bulk_save_objects(results)
        db.session.commit()

        return jsonify({"message": "Results imported successfully", "imported_count": len(results)})

    return jsonify({"message": "Failed to import results."}), 500 """