import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Landing from './pages/Landing';
import Register from './pages/Register';
import SignIn from './pages/SignIn';
import Profile from './pages/Profile';
import Notifications from './pages/Notifications';
import Messages from './pages/Messages';
import SavedPosts from './pages/SavedPosts';
import Search from './pages/Search';
import Home from './pages/Home';
import './assets/styles/App.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="*"
            element={
              <>
                <Sidebar />
                <div className="main-content">
                  <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/profile/:id" element={<Profile />} />
                    <Route path="/notifications" element={<Notifications />} />
                    <Route path="/messages" element={<Messages />} />
                    <Route path="/saved-posts" element={<SavedPosts />} />
                    <Route path="/search" element={<Search />} />
                  </Routes>
                </div>
              </>
            }
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
