import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '../assets/styles/Profile.css';

const Profile = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    profile_photo: '',
    bio: '',
    location: '',
    contact_info: ''
  });

  useEffect(() => {
    const fetchUserData = async () => {
      const token = localStorage.getItem('token');
      console.log('Token_profile:', token);  // Debug log
      if (!token) {
        setError('No token found');
        setLoading(false);
        return;
      }

      try {
        console.log('Fetching user data for ID:', id);  // Debug log

        const response = await fetch(`http://localhost:5000/api/users/${id}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        console.log('Response status:', response.status);  // Debug log
        const data = await response.json();
        console.log('Response data:', data);  // Debug log

        if (response.ok) {
          setUser(data);
          setFormData({
            name: data.name,
            email: data.email,
            profile_photo: data.profile_photo,
            bio: data.bio,
            location: data.location,
            contact_info: data.contact_info
          });
        } else {
          setError(data.message || 'Error fetching user data');
        }
      } catch (err) {
        console.error('Fetch error:', err);  // Debug log
        setError('Failed to fetch user data');
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleUpdate = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      setError('No token found');
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/api/users/${id}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        const data = await response.json();
        setUser(data);
        setEditMode(false);
      } else {
        const data = await response.json();
        setError(data.message || 'Error updating user data');
      }
    } catch (err) {
      console.error('Update error:', err);  // Debug log
      setError('Failed to update user data');
    }
  };

  const handleDelete = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      setError('No token found');
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/api/users/${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        navigate('/');  // Redirect to another page after deletion
      } else {
        const data = await response.json();
        setError(data.message || 'Error deleting user');
      }
    } catch (err) {
      console.error('Delete error:', err);  // Debug log
      setError('Failed to delete user');
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;
  if (!user) return <div>No user data available</div>;

  return (
    <div className="profile-container">
      <h1>{editMode ? 'Edit Profile' : user.name}</h1>
      <div className="profile-field">
        <label>Email:</label>
        {editMode ? <input type="email" name="email" value={formData.email} onChange={handleInputChange} /> : <span>{user.email}</span>}
      </div>
      <div className="profile-field">
        <label>Profile Photo:</label>
        {editMode ? <input type="text" name="profile_photo" value={formData.profile_photo} onChange={handleInputChange} /> : <span>{user.profile_photo}</span>}
      </div>
      <div className="profile-field">
        <label>Bio:</label>
        {editMode ? <input type="text" name="bio" value={formData.bio} onChange={handleInputChange} /> : <span>{user.bio}</span>}
      </div>
      <div className="profile-field">
        <label>Location:</label>
        {editMode ? <input type="text" name="location" value={formData.location} onChange={handleInputChange} /> : <span>{user.location}</span>}
      </div>
      <div className="profile-field">
        <label>Contact Info:</label>
        {editMode ? <input type="text" name="contact_info" value={formData.contact_info} onChange={handleInputChange} /> : <span>{user.contact_info}</span>}
      </div>
      <div className="profile-actions">
        {editMode ? (
          <button className="btn-update" onClick={handleUpdate}>Update</button>
        ) : (
          <button className="btn-edit" onClick={() => setEditMode(true)}>Edit</button>
        )}
        <button className="btn-delete" onClick={handleDelete}>Delete</button>
      </div>
    </div>
  );
};

export default Profile;
