from flask import Blueprint, request, jsonify
from app.models import User, Post, Comment, Like
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

posts_bp = Blueprint('posts_bp', __name__)

@posts_bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    user_id = get_jwt_identity()

    # Add logging to debug
    print(f"Received data: {data}")
    print(f"User ID: {user_id}")

    if not data:
        return jsonify({"message": "No data provided"}), 400

    required_fields = ['group', 'image', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing field: {field}"}), 400

    new_post = Post(
        user_id=user_id,
        group=data['group'],
        image=data['image'],
        description=data['description']
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200

@posts_bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    new_comment = Comment(
        post_id=post_id,
        user_id=user_id,
        content=data['content']
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment.to_dict()), 201

@posts_bp.route('/posts/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    user_id = get_jwt_identity()
    like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return jsonify({"message": "Like removed"}), 200
    else:
        new_like = Like(post_id=post_id, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()
        return jsonify({"message": "Post liked"}), 201
