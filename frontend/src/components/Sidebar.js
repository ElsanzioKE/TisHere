import React from 'react';
import { NavLink } from 'react-router-dom';
import '../assets/styles/Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>TisHere</h2>
      <ul>
        <li>
          <NavLink to="/" exact activeClassName="active-link">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/profile" activeClassName="active-link">
            Profile
          </NavLink>
        </li>
        <li>
          <NavLink to="/notifications" activeClassName="active-link">
            Notifications
          </NavLink>
        </li>
        <li>
          <NavLink to="/messages" activeClassName="active-link">
            Messages
          </NavLink>
        </li>
        <li>
          <NavLink to="/saved-posts" activeClassName="active-link">
            Saved Posts
          </NavLink>
        </li>
        <li>
          <NavLink to="/search" activeClassName="active-link">
            Search
          </NavLink>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
