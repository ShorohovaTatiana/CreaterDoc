from Backend.entities.User import User
from flask import Blueprint, request, session, redirect, jsonify
from main_config import db
from Backend.Utils import Utils

user = Blueprint('user', __name__)

@user.route('/api/login', methods=['POST'])
def api_user_auth():
    request_data = request.get_json()
    email = request_data['email'].strip()
    password = request_data['password'].strip()
    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify(message="User with this login was not found"), 400
    if user.password != Utils.get_hash(password):
        return jsonify(message="Password is no correct"), 400
    if 'user_id' not in session:
        session['user_id'] = user.id
    return jsonify(), 200


@user.route('/api/registration', methods=['POST'])
def api_user_registration():
    request_data = request.get_json()
    email = request_data['email'].strip()
    already_user = User.query.filter_by(email=email).first()
    if already_user is not None:
        return jsonify(message="User with this login already registrated"), 400
    password = request_data['password'].strip()
    if len(password) < 6:
        return jsonify(message="Password is no correct"), 400
    password = Utils.get_hash(password)
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(), 200


@user.route('/logout')
def logout():
    if 'user_id' in session:
        session.modified = True
        for key in list(session.keys()):
            session.pop(key)
        session.modified = True
    return redirect('/login')