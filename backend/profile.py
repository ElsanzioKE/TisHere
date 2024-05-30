#!/usr/bin/python3
from flask import request, jsonify
from app import app, db
from app.models import Profile

@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    new_profile = Profile(
        user_name=data['user_name'],
        education=data.get('education', ''),
        experience=data.get('experience', '')
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify(new_profile.serialize()), 201

@app.route('/profiles/<int:id>', methods=['GET'])
def get_profile(id):
    profile = Profile.query.get_or_404(id)
    return jsonify(profile.serialize())

@app.route('/profiles/<int:id>', methods=['PUT'])
def update_profile(id):
    data = request.get_json()
    profile = Profile.query.get_or_404(id)

    profile.user_name = data.get('user_name', profile.user_name)
    profile.education = data.get('education', profile.education)
    profile.experience = data.get('experience', profile.experience)

    db.session.commit()
    return jsonify(profile.serialize())

@app.route('/profiles/<int:id>', methods=['DELETE'])
def delete_profile(id):
    profile = Profile.query.get_or_404(id)
    db.session.delete(profile)
    db.session.commit()
    return '', 204

