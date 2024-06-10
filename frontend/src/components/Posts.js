import React from 'react';

const Posts = ({ id, content, media_url, user_id, likes }) => {
    const handleLike = async () => {
        const token = localStorage.getItem('token');
        if (!token) {
            console.error('No token found');
            return;
        }

        try {
            const response = await fetch(`http://localhost:5000/api/posts/${id}/like`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                console.error('Error liking post:', response.statusText);
            }
        } catch (error) {
            console.error('Error liking post:', error);
        }
    };

    const handleUnlike = async () => {
        const token = localStorage.getItem('token');
        if (!token) {
            console.error('No token found');
            return;
        }

        try {
            const response = await fetch(`http://localhost:5000/api/posts/${id}/like`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                console.error('Error unliking post:', response.statusText);
            }
        } catch (error) {
            console.error('Error unliking post:', error);
        }
    };

    return (
        <div className="post">
            <p>{content}</p>
            {media_url && <img src={media_url} alt="Post media" />}
            <div>
                <button onClick={handleLike}>Like</button>
                <button onClick={handleUnlike}>Unlike</button>
            </div>
            <p>{likes?.length} Likes</p>
        </div>
    );
};

export default Posts;
