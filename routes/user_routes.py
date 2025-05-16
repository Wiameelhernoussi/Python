from flask import Blueprint, request, jsonify
from auth.jwt_auth import generate_token

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username == "admin" and password == "admin":
        token = generate_token(user_id=1)
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401
