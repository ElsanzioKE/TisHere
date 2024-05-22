// src/components/Communities.js
import React from 'react';
import '../assets/styles/Communities.css';

function Communities({ communities }) {
  return (
    <div className="communities">
      <h3>Communities you might like</h3>
      <ul>
        {communities.map(community => (
          <li key={community.id}>
            <div>
              <strong>{community.name}</strong>
              <p>{community.members} members</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Communities;
