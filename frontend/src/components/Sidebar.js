import React from 'react';
import { NavLink } from 'react-router-dom';
import '../assets/styles/Sidebar.css';

const Sidebar = () => {
  const userId = 1; // Replace this with actual user ID logic

  return (
    <div className="sidebar">
      <h2>TisHere</h2>
      <ul>
        <li>
          <NavLink
            to="/home"
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink
            to={`/profile/${userId}`}
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Profile
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/notifications"
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Notifications
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/messages"
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Messages
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/saved-posts"
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Saved Posts
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/search"
            className={({ isActive }) => (isActive ? 'active-link' : '')}
          >
            Search
          </NavLink>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
