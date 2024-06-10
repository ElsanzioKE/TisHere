import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Posts from "../components/Posts";
import SuggestedPeople from "../components/SuggestedPeople";
import Communities from "../components/Communities";
import CreatePost from "../components/CreatePost";
import '../assets/styles/Home.css';

function Home() {
    const [posts, setPosts] = useState([]);
    const [suggestedPeople, setSuggestedPeople] = useState([]);
    const [communities, setCommunities] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            const token = localStorage.getItem('token');
            if (!token) {
                console.error('No token found');
                return;
            }

            try {
                const response = await fetch('http://localhost:5000/api/posts', {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'application/json',
                    },
                });

                if (response.ok) {
                    const data = await response.json();
                    setPosts(data);
                } else {
                    console.error('Error fetching posts:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        };

        const fetchSuggestedPeople = async () => {
            // Fetch suggested people logic
            // Placeholder: setSuggestedPeople([...]);
        };

        const fetchCommunities = async () => {
            // Fetch communities logic
            // Placeholder: setCommunities([...]);
        };

        fetchPosts();
        fetchSuggestedPeople();
        fetchCommunities();
    }, []);

    const addPost = (post) => {
        setPosts([post, ...posts]);
    };

    return (
        <div className="home">
            <div className="main-content">
                <Navbar />
                <CreatePost addPost={addPost} />
                <div className="posts">
                    {posts.map((post, index) => (
                        <Posts key={index} {...post} />
                    ))}
                </div>
                <div className="sidebar-right">
                    <SuggestedPeople people={suggestedPeople} />
                    <Communities communities={communities} />
                </div>
            </div>
        </div>
    );
}

export default Home;
