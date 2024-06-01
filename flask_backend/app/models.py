from .extensions import db
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class BaseModel(db.Model):
    """Base model for all models"""
    __abstract__ = True

    id = db.Column(db.String(60), unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

class User(BaseModel):
    """User model"""
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(128), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    contact_info = db.Column(db.String(128), nullable=True)

    posts = db.relationship('Post', backref='user', cascade='all, delete')
    comments = db.relationship('Comment', backref='user', cascade='all, delete')
    likes = db.relationship('Like', backref='user', cascade='all, delete')
    groups = db.relationship('Group', secondary='user_groups', back_populates='users')

class Post(BaseModel):
    """Post model"""
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    comments = db.relationship('Comment', backref='post', cascade='all, delete')
    likes = db.relationship('Like', backref='post', cascade='all, delete')
