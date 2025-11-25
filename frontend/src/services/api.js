import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Auth APIs
export const authAPI = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', new URLSearchParams(data), {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  }),
  getMe: () => api.get('/auth/me'),
};

// Project APIs
export const projectAPI = {
  list: () => api.get('/projects'),
  create: (data) => api.post('/projects', data),
  get: (id) => api.get(`/projects/${id}`),
  delete: (id) => api.delete(`/projects/${id}`),
  generateContent: (projectId) => api.post('/projects/generate-content', { project_id: projectId }),
  updateSection: (sectionId, data) => api.put(`/projects/sections/${sectionId}`, data),
  refineContent: (sectionId, prompt) => api.post('/projects/refine-content', { section_id: sectionId, prompt }),
  aiSuggest: (data) => api.post('/projects/ai-suggest', data),
  export: (id) => api.get(`/projects/${id}/export`, { responseType: 'blob' }),
};

export default api;
