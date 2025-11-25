import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { projectAPI } from '../services/api';
import './Dashboard.css';

function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      const response = await projectAPI.list();
      setProjects(response.data);
    } catch (err) {
      setError('Failed to load projects');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteProject = async (projectId, e) => {
    e.stopPropagation();
    if (!window.confirm('Are you sure you want to delete this project?')) {
      return;
    }

    try {
      await projectAPI.delete(projectId);
      setProjects(projects.filter(p => p.id !== projectId));
    } catch (err) {
      alert('Failed to delete project');
      console.error(err);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
    });
  };

  return (
    <div className="dashboard-container">
      <nav className="dashboard-nav">
        <div className="nav-content">
          <h1 className="nav-title">PresentWallah</h1>
          <div className="nav-user">
            <span>Welcome, {user?.username}</span>
            <button onClick={logout} className="logout-button">Logout</button>
          </div>
        </div>
      </nav>

      <div className="dashboard-content">
        <div className="dashboard-header">
          <h2>My Projects</h2>
          <button 
            className="create-button"
            onClick={() => navigate('/create-project')}
          >
            + New Project
          </button>
        </div>

        {error && <div className="error-message">{error}</div>}

        {loading ? (
          <div className="loading">Loading projects...</div>
        ) : projects.length === 0 ? (
          <div className="empty-state">
            <h3>No projects yet</h3>
            <p>Create your first AI-powered document</p>
            <button 
              className="create-button"
              onClick={() => navigate('/create-project')}
            >
              + Create Project
            </button>
          </div>
        ) : (
          <div className="projects-grid">
            {projects.map((project) => (
              <div 
                key={project.id} 
                className="project-card"
                onClick={() => navigate(`/project/${project.id}`)}
              >
                <div className="project-header">
                  <div className={`project-type ${project.document_type}`}>
                    {project.document_type.toUpperCase()}
                  </div>
                  <button 
                    className="delete-button"
                    onClick={(e) => handleDeleteProject(project.id, e)}
                  >
                    ×
                  </button>
                </div>
                <h3 className="project-title">{project.title}</h3>
                <p className="project-topic">{project.main_topic}</p>
                <div className="project-footer">
                  <span className="project-date">
                    Updated: {formatDate(project.updated_at)}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;
