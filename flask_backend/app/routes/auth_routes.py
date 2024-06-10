from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.auth_service import authenticate_user
from app.config import Config
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@jwt_required()
@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user, token = authenticate_user(email, password)
    if user:
        return jsonify({
            'token': token,
            'user_id': user.id,
            'user_name': user.name,
            'user_email': user.email
        }), 200
    return jsonify({"message": "Invalid credentials"}), 401
