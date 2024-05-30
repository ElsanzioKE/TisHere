from .extensions import db
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, ForeignKey

Base = declarative_base()

class BaseModel(Base):
    """Base model for all models"""
    __abstract__ = True
     
     id = Column(String(60), unique=True, primary_key=True, default=uuid.uuid4)
     created_at = Column(DateTime, nullable= False, default=datetime.utcnow())
     updated_at = Column(DateTime, nullable= False, default=datetime.utcnow())

class User(BaseModel):
    """User model"""
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    profile_photo = Column(String(128), nullable=True)
    bio = Column(Text, nullable=True)
    contact_info = Column(String(128), nullable=True)
    posts = relationship('Post', backref='user', cascade='all, delete')
    comments = relationship('Comment', backref='user', cascade='all, delete')
    likes = relationship('Like', backref='user', cascade='all, delete')
    groups = relationship('Group', secondary='user_groups', back_populates='users')

class Post(BaseModel):
    """Post model"""
    __tablename__ = 'posts'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')
    content = Column(Text, nullable=False)
    comments = relationship('Comment', backref='post', cascade='all, delete')
    likes = relationship('Like', backref='post', cascade='all, delete')

