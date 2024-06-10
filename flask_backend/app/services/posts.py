from app.models import Post, Like
from app.extensions import db
from uuid import uuid4

def create_post(user_id, content, media_url=None):
    post = Post(id=str(uuid4()), user_id=user_id, content=content, media_url=media_url)
    db.session.add(post)
    db.session.commit()
    return post

def get_all_posts():
    return Post.query.order_by(Post.created_at.desc()).all()

def like_post(user_id, post_id):
    like = Like(id=str(uuid4()), user_id=user_id, post_id=post_id)
    db.session.add(like)
    db.session.commit()
    return like

def unlike_post(user_id, post_id):
    like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return like
    return None
