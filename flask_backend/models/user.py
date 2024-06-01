#!/usr/bin/python3
"""User model"""


from sqlalchemyimport Column, String, ForeignKey, Text
#from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel):
    """User model"""
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    profile_photo = Column(String(128), nullable=True)
    bio = Column(Text, nullable=True)
    contact_info = Column(String(128), nullable=True)
    """
    posts = relationship('Post', backref='user', cascade='all, delete')
    comments = relationship('Comment', backref='user', cascade='all, delete')
    likes = relationship('Like', backref='user', cascade='all, delete')
    groups = relationship('Group', secondary='user_groups', back_populates='users')
    """
    

    