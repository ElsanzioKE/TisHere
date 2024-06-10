from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user import create_user, get_user, get_all_users, update_user, delete_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/users', methods=['POST'])
def create_user_route():
    """Creates a new user"""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    try:
        user = create_user(name, email, password)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/api/users/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user_route(user_id):
    """Gets user by ID"""
    user = get_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/api/users/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = get_user(current_user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/api/users', methods=['GET'])
def get_all_users_route():
    """Gets all users"""
    users = get_all_users()
    return jsonify([user.to_dict() for user in users]), 200


@user_bp.route('/api/users/<string:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    """Updates user"""
    data = request.get_json()
    user = update_user(user_id, **data)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found!'}), 404

@user_bp.route('/api/users/<string:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    """Deletes user"""
    user = delete_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found!'}), 404


