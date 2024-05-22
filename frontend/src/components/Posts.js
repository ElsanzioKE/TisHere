// src/components/Post.js
import React from 'react';
import '../assets/styles/Posts.css';

function Post({ user, group, time, image, description, likes, comments }) {
  return (
    <div className="post">
      <div className="post-header">
        <img src={user.avatar} alt={user.name} className="avatar" />
        <div>
          <strong>{user.name}</strong> in {group}
          <p>{time}</p>
        </div>
      </div>
      <img src={image} alt="Post" className="post-image" />
      <p>{description}</p>
      <div className="post-footer">
        <span>{likes} likes</span>
        <span>{comments} comments</span>
      </div>
    </div>
  );
}

export default Post;
