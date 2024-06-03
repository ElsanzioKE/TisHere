from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(name, email, password, **kwargs):
    """ creates a new user"""
    hashed_password = generate_password_hash(password)
    new_user = User(name=name,
        email=email,
        password=hashed_password,
        **kwargs
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user(user_id):
    """gets user by id"""
    return User.querry.get(user_id)

def get_all_users():
    """gets all users"""
    return User.querry.all()

def update_user(user_id, **kwargs):
    """updates user"""
    user = get_user(user_id)
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
            db.session.commit()
        return user

def delete_user(user_id):
    user  = get_user(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user