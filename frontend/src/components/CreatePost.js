import React, { useState } from 'react';

const CreatePost = ({ addPost }) => {
    const [content, setContent] = useState('');
    const [mediaUrl, setMediaUrl] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');
        if (!token) {
            setError('No token found');
            return;
        }

        try {
            const response = await fetch('http://localhost:5000/api/posts', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content, media_url: mediaUrl })
            });

            if (response.ok) {
                const data = await response.json();
                addPost(data);
                setContent('');
                setMediaUrl('');
            } else {
                const responseData = await response.json();
                setError(responseData.message || 'Error creating post');
            }
        } catch (error) {
            setError('Failed to create post');
        }
    };

    return (
        <div className="create-post">
            <form onSubmit={handleSubmit}>
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder="Write a post..."
                />
                <input
                    type="text"
                    value={mediaUrl}
                    onChange={(e) => setMediaUrl(e.target.value)}
                    placeholder="Media URL (optional)"
                />
                <button type="submit">Post</button>
            </form>
            {error && <div className="error">{error}</div>}
        </div>
    );
};

export default CreatePost;
