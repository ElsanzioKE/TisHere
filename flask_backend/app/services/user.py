from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(name, email, password, **kwargs):
    """Creates a new user"""
    if User.query.filter_by(email=email).first():
        raise ValueError("Email already exists")
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password, **kwargs)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user(user_id):
    """Gets user by ID"""
    user = User.query.get(user_id)
    print(f"Queried user: {user}")
    return user

def get_all_users():
    """Gets all users"""
    return User.query.all()

def update_user(user_id, **kwargs):
    """Updates user"""
    user = get_user(user_id)
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user
    return None

def delete_user(user_id):
    """Deletes user"""
    user = get_user(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user
    return None
