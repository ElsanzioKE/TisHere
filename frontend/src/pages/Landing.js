import React from 'react';
import { Link } from 'react-router-dom';
import '../assets/styles/Landing.css'; // Create this CSS file for styling the landing page

const Landing = () => {
  return (
    <div className="landing-page">
      <h1>Welcome to TisHere</h1>
      <p>Do you have an account?</p>
      <div className="landing-buttons">
        <Link to="/signin" className="btn">Sign In</Link>
        <Link to="/register" className="btn">Register</Link>
      </div>
    </div>
  );
};

export default Landing;
