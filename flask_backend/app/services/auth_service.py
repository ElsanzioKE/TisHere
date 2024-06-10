from app.models import User
from werkzeug.security import check_password_hash
import jwt
import datetime
from flask import current_app
from flask_jwt_extended import create_access_token

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        token = create_access_token(identity=user.id)
        return user, token
    return None, None
