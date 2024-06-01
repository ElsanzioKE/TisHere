from .extensions import db
import uuid
from datetime import datetime

class BaseModel(db.Model):
    """Base model for all models"""
    __abstract__ = True

    id = db.Column(db.String(60), unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(BaseModel):
    """User model"""
    __tablename__ = 'users'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(128), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(128), nullable=True)
    contact_info = db.Column(db.String(128), nullable=True)

    posts = db.relationship('Post', backref='user', cascade='all, delete')
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='all, delete')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', cascade='all, delete')
    received_messages = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', cascade='all, delete')
    groups = db.relationship('Group', secondary='user_groups', back_populates='users')
    rsvps = db.relationship('Event', secondary='user_events', back_populates='users')
    connections = db.relationship('Connection', foreign_keys='Connection.user_id', backref='user', cascade='all, delete')
    connected_users = db.relationship('Connection', foreign_keys='Connection.connected_user_id', backref='connected_user', cascade='all, delete')
    notifications = db.relationship('Notification', backref='user', cascade='all, delete')
    job_applications = db.relationship('JobApplication', backref='user', cascade='all, delete')

class Profile(BaseModel):
    """Profile model"""
    __tablename__ = 'profiles'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    skills = db.Column(db.Text, nullable=True)
    interests = db.Column(db.Text, nullable=True)
    experience = db.Column(db.Text, nullable=True)
    education = db.Column(db.Text, nullable=True)
    visibility_settings = db.Column(db.Text, nullable=True)

class Post(BaseModel):
    """Post model"""
    __tablename__ = 'posts'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(256), nullable=True)

    comments = db.relationship('Comment', backref='post', cascade='all, delete')
    likes = db.relationship('Like', backref='post', cascade='all, delete')

class Comment(BaseModel):
    """Comment model"""
    __tablename__ = 'comments'
    post_id = db.Column(db.String(60), db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Like(BaseModel):
    """Like model"""
    __tablename__ = 'likes'
    post_id = db.Column(db.String(60), db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)

class Message(BaseModel):
    """Message model"""
    __tablename__ = 'messages'
    sender_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    read_at = db.Column(db.DateTime, nullable=True)

class Group(BaseModel):
    """Group model"""
    __tablename__ = 'groups'
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)

    users = db.relationship('User', secondary='user_groups', back_populates='groups')
    group_posts = db.relationship('GroupPost', backref='group', cascade='all, delete')

class GroupPost(BaseModel):
    """GroupPost model"""
    __tablename__ = 'group_posts'
    group_id = db.Column(db.String(60), db.ForeignKey('groups.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(256), nullable=True)

    comments = db.relationship('Comment', backref='group_post', cascade='all, delete')
    likes = db.relationship('Like', backref='group_post', cascade='all, delete')

class Event(BaseModel):
    """Event model"""
    __tablename__ = 'events'
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(128), nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    users = db.relationship('User', secondary='user_events', back_populates='rsvps')
    event_posts = db.relationship('EventPost', backref='event', cascade='all, delete')

class EventPost(BaseModel):
    """EventPost model"""
    __tablename__ = 'event_posts'
    event_id = db.Column(db.String(60), db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(256), nullable=True)

    comments = db.relationship('Comment', backref='event_post', cascade='all, delete')
    likes = db.relationship('Like', backref='event_post', cascade='all, delete')

class Connection(BaseModel):
    """Connection model"""
    __tablename__ = 'connections'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    connected_user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Notification(BaseModel):
    """Notification model"""
    __tablename__ = 'notifications'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    read_status = db.Column(db.Boolean, nullable=False, default=False)

class Job(BaseModel):
    """Job model"""
    __tablename__ = 'jobs'
    company_id = db.Column(db.String(60), db.ForeignKey('companies.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(128), nullable=True)
    requirements = db.Column(db.Text, nullable=True)

    applications = db.relationship('JobApplication', backref='job', cascade='all, delete')

class JobApplication(BaseModel):
    """JobApplication model"""
    __tablename__ = 'job_applications'
    job_id = db.Column(db.String(60), db.ForeignKey('jobs.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    resume = db.Column(db.Text, nullable=True)
    cover_letter = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='pending')
    applied_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Company(BaseModel):
    """Company model"""
    __tablename__ = 'companies'
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(128), nullable=True)
    website = db.Column(db.String(128), nullable=True)

    jobs = db.relationship('Job', backref='company', cascade='all, delete')

# Association tables for many-to-many relationships
user_groups = db.Table('user_groups',
    db.Column('user_id', db.String(60), db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.String(60), db.ForeignKey('groups.id'), primary_key=True)
)

user_events = db.Table('user_events',
    db.Column('user_id', db.String(60), db.ForeignKey('users.id'), primary_key=True),
    db.Column('event_id', db.String(60), db.ForeignKey('events.id'), primary_key=True)
)
