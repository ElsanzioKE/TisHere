from flask import Blueprint, request, jsonify
from app.services.user import create_user, get_user, get_all_users, update_user, delete_user

user_bp = Blueprint('user', __name__)
@user_bp.route('/users', methods=['POST'])
def create_user():
    """creates a new user"""
    data = request.get_json()
    name  = data['name']
    email = data['email']
    password = data['password']

    data.pop('name')
    data.pop('email')
    data.pop('password')

    user = create_user(name, email, password, **data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/users/user_id', methods=['GET'])
def get_user(user_id):
    """gets user by id"""
    user = get_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    """gets all users"""
    users = get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """updates user"""
    data = request.get_json()
    user = update_user(user_id, **data)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found!'}), 404

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """deletes user"""
    user = delete_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found!'}), 404
