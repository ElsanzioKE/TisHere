// src/components/SuggestedPeople.js
import React from 'react';
import '../assets/styles/SuggestedPeople.css';

function SuggestedPeople({ people }) {
  return (
    <div className="suggested-people">
      <h3>Suggested people</h3>
      <ul>
        {people.map(person => (
          <li key={person.id}>
            <img src={person.avatar} alt={person.name} />
            <div>
              <strong>{person.name}</strong>
              <p>@{person.username}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SuggestedPeople;
