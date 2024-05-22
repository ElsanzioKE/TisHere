import React  from "react";
import Navbar from "../components/Navbar";
import Posts from "../components/Posts"
import SuggestedPeople from "../components/SuggestedPeople";
import Communities from "../components/Communities";
import '../assets/styles/Home.css';
function Home() {
    const samplePosts = [
        {
          user: { name: 'Helena', avatar: 'path/to/avatar.jpg' },
          group: 'Group name',
          time: '3 min ago',
          image: 'path/to/image.jpg',
          description: 'Post description',
          likes: 21,
          comments: 4,
        },
        {
            user: { name: 'Lesuuda', avatar: '/images/lesuuda.jpg' },
            group: 'Sambwenya',
            time: '0 min ago',
            image: '/images/kenya_power.jpeg',
            description: 'An accident just occured involving a Kenya Power Vehicle',
            likes: 21,
            comments: 4,
          },
          {
            user: { name: 'Helena', avatar: 'path/to/avatar.jpg' },
            group: 'Group name',
            time: '3 min ago',
            image: 'path/to/image.jpg',
            description: 'Post description',
            likes: 21,
            comments: 4,
          },
        // Add more sample posts here
      ];
      const suggestedPeople = [
        { id: 1, name: 'Helena Hills', username: 'helenahills', avatar: 'path/to/avatar.jpg' },
        // Add more people
      ];
    
      const communities = [
        { id: 1, name: 'Design Enthusiasts', members: '13.2k' },
        // Add more communities
      ];
    
    return (
        <div className="home">
            <div className="main-content">
                <Navbar />
                <div className="posts">
                    {samplePosts.map((post, index) => (
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