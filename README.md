# PresentWallah - AI-Powered Document Creation Platform

## 🌊 Overview

PresentWallah is a full-stack AI-powered web application that enables authenticated users to generate, refine, and export professional business documents (Word .docx and PowerPoint .pptx files). The platform leverages Groq's LLM API (llama-3.3-70b-versatile) to provide intelligent, executive-level content generation with comprehensive revision tracking.

## ✨ Features

### Core Functionality
- **User Authentication**: Secure JWT-based registration and login system with bcrypt password hashing
- **Project Management**: Create, view, manage, and delete multiple document projects
- **Document Types**: Full support for Word documents (.docx) and PowerPoint presentations (.pptx)
- **AI-Powered Content Generation**: Automated executive-level content generation using Groq LLM (llama-3.3-70b-versatile)
- **Enhanced AI Prompts**: Professional C-suite quality content with specific metrics, frameworks, and actionable insights

### PowerPoint Features
- **Multi-Template System**: Choose from 4 professional templates:
  - **Modern**: Navy blue theme with clean layouts
  - **Minimal**: Sophisticated gray aesthetic
  - **Corporate**: Professional blue corporate style
  - **Creative**: Bold purple creative design
- **Customizable Font Sizes**: Adjustable base font size (16-28pt) for all slides
- **Professional Color Schemes**: Each template includes coordinated color palettes
- **Automatic Image Integration**: Smart stock photo insertion from Pexels API
- **Live Slide Preview**: Real-time preview with images before export

### Content Management
- **AI Outline Suggestion**: Intelligent outline/slide structure generation based on main topic
- **Interactive Refinement System**: 
  - Real-time content refinement with AI
  - Like/Dislike feedback buttons (persisted to database)
  - Section-specific comments and notes (fully persisted)
  - **Complete Revision History Tracking** - every refinement saved with:
    - Original refinement prompt
    - Content before refinement
    - Content after refinement
    - Timestamp
- **Manual Editing**: Reorder sections, add/remove slides, customize titles
- **Document Export**: Download completed documents in native .docx or .pptx format with embedded images

### User Interface
- **Modern Glassmorphism Design**: Professional UI with backdrop blur effects
- **Smooth Animations**: Fade-in, slide, and scale animations throughout
- **Responsive Layout**: Clean, professional interface with cyan accent theme
- **Staggered Card Animations**: Elegant project card entrance effects
- **Hover Effects**: Lift effects with cyan glow on interactive elements
- **Inter Font Typography**: Modern, professional typography

## 🏗️ Architecture

### Backend (FastAPI)
- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT tokens with bcrypt password hashing
- **LLM Integration**: Groq API (llama-3.3-70b-versatile model)
- **Image Integration**: Pexels API for stock photos (optional, free)
- **Document Generation**: python-docx and python-pptx libraries

### Frontend (React)
- **Framework**: React 18 with Vite
- **Routing**: React Router v6
- **API Communication**: Axios
- **State Management**: Context API (AuthContext)
- **Styling**: Custom CSS with glassmorphism, animations, and modern design patterns
- **Typography**: Inter font family from Google Fonts
- **UI Features**: Backdrop blur, gradient effects, smooth transitions, staggered animations

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- Groq API Key (get one from [Groq Console](https://console.groq.com))
- Pexels API Key (optional, for images - get from [Pexels API](https://www.pexels.com/api/))

## 🚀 Installation & Setup

### Quick Start (Recommended)

**For Windows PowerShell users**, use the automated startup script:

```powershell
cd PresentWallah
.\start.ps1
```

This will automatically:
- Start the backend server on port 8000
- Start the frontend server on port 3000
- Open in separate windows for easy monitoring

**Access the application**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

Press any key in the startup terminal to stop all servers.

---

### Manual Setup

If you prefer manual setup or are on a different platform, follow these detailed instructions:

### Backend Setup

1. **Navigate to the backend directory**:
   ```powershell
   cd backend
   ```

2. **Create a virtual environment**:
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
   
   **Note**: If you encounter bcrypt compatibility issues, the application uses bcrypt 4.0.1. This is automatically installed from requirements.txt.

5. **Configure environment variables**:
   
   Create a `.env` file in the `backend` directory:
   ```env
   SECRET_KEY=your-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   GROQ_API_KEY=your-groq-api-key-here
   PEXELS_API_KEY=your-pexels-api-key-here
   DATABASE_URL=sqlite:///./presentwallah.db
   ```

   **Important**: 
   - Replace `your-groq-api-key-here` with your actual Groq API key from [Groq Console](https://console.groq.com)
   - (Optional) Replace `your-pexels-api-key-here` with your Pexels API key for automatic images in presentations. Get it free from [Pexels API](https://www.pexels.com/api/)
   - For production, use a strong random SECRET_KEY (generate with `openssl rand -hex 32`)

6. **Run database migrations** (if needed):
   ```powershell
   python migrate_db.py
   ```
   This ensures the database has the latest schema with template and font_size columns.

7. **Run the backend server**:
   ```powershell
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The backend API will be available at `http://localhost:8000`
   API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Open a new terminal and navigate to the frontend directory**:
   ```powershell
   cd frontend
   ```

2. **Install dependencies**:
   ```powershell
   npm install
   ```

3. **Start the development server**:
   ```powershell
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## 🔑 Environment Variables

### Backend (.env)

Create a `.env` file in the `backend/` directory with the following variables:

| Variable | Description | Required | Default | Example |
|----------|-------------|----------|---------|---------|
| `SECRET_KEY` | Secret key for JWT token generation and security | ✅ Yes | - | `your-super-secret-key-min-32-chars` |
| `ALGORITHM` | JWT signing algorithm | No | `HS256` | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time in minutes | No | `30` | `30` |
| `GROQ_API_KEY` | Your Groq API key for LLM | ✅ Yes | - | `gsk_xxxxxxxxxxxxx` |
| `PEXELS_API_KEY` | Your Pexels API key for stock images | No | - | `7NmYpMktvDJMB4...` |
| `DATABASE_URL` | SQLite database connection string | No | `sqlite:///./presentwallah.db` | `sqlite:///./presentwallah.db` |

**How to get API keys:**
1. **Groq API Key**: 
   - Sign up at [Groq Console](https://console.groq.com)
   - Create a new API key
   - Copy and paste into `.env`

2. **Pexels API Key** (Optional for images):
   - Sign up at [Pexels API](https://www.pexels.com/api/)
   - Free tier available (200 requests/hour)
   - Copy and paste into `.env`

**Example `.env` file:**
```env
SECRET_KEY=your-secret-key-here-generate-with-openssl
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GROQ_API_KEY=your-groq-api-key-here
PEXELS_API_KEY=your-pexels-api-key-here
DATABASE_URL=sqlite:///./presentwallah.db
```

### Frontend Configuration

No environment variables required for frontend. API base URL is configured in `src/services/api.js` and uses relative paths with Vite proxy.

## 📖 Usage Guide

### 1. Registration & Login

1. Navigate to `http://localhost:3000`
2. Click "Sign Up" to create a new account
3. Enter email, username, and password
4. After registration, login with your credentials

### 2. Creating a New Project

1. From the dashboard, click "+ New Project"
2. **Step 1**: Choose document type (Word or PowerPoint)
3. **Step 2**: Configure your project:
   - Enter project title
   - Enter main topic/description
   - **For PowerPoint**: Select template (Modern/Minimal/Corporate/Creative)
   - **For PowerPoint**: Adjust font size slider (16-28pt)
   - **Option A**: Click "AI-Suggest Outline" for AI-generated structure
   - **Option B**: Manually add sections/slides using the "+ Add" button
   - Reorder sections using ↑/↓ buttons
   - Remove unwanted sections with × button
4. Click "Create Project"

### 3. Generating Content

1. Open a project from the dashboard
2. Click "Generate Content" button
3. AI will generate professional, executive-level content for all sections/slides
4. Content includes:
   - **For PowerPoint**: 4-6 concise bullet points with metrics and frameworks
   - **For Word**: 300-500 word paragraphs with specific insights and actionable takeaways
5. Wait for generation to complete

### 4. Refining Content

For each section/slide, you have multiple options:

- **Like/Dislike Feedback**: 
  - Click "Like" or "Dislike" buttons
  - Feedback is **permanently saved** to the database
  
- **AI Refinement**: 
  - Enter a refinement prompt (e.g., "Add more statistics", "Make it more technical", "Simplify for executives")
  - Click "Refine Content"
  - AI regenerates content based on your instructions
  - **Complete revision history saved** including:
    - Your refinement prompt
    - Previous content version
    - New refined content
    - Timestamp
  
- **Add Comments**: 
  - Use the comment section to add personal notes
  - Comments are **permanently persisted** to database
  
- **View Revision History**:
  - All refinements are tracked in the `revisions` table
  - Use `show_db.py` to view complete revision history

### 5. Exporting Documents

1. After generating and refining content, click "Export Document"
2. The file will download in the appropriate format:
   - **.docx**: Word document with formatted paragraphs
   - **.pptx**: PowerPoint with selected template, custom font size, and embedded images from Pexels
3. Open with Microsoft Word or PowerPoint

### 6. Viewing Database & Revision History

To inspect your data and revision history:

```powershell
cd backend
python show_db.py
```

This displays:
- Database structure
- Number of sections and revisions
- Latest refinement details
- Complete audit trail

## 🗂️ Project Structure

```
PresentWallah/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy database models
│   │   │   ├── user.py      # User authentication model
│   │   │   ├── project.py   # Project model with template/font_size
│   │   │   ├── section.py   # Section model with content/comments/feedback
│   │   │   └── revision.py  # Revision history tracking
│   │   ├── routers/         # API route handlers
│   │   │   ├── auth.py      # Authentication endpoints
│   │   │   └── projects.py  # Project CRUD + AI operations
│   │   ├── services/        # Business logic services
│   │   │   ├── auth.py      # JWT & password hashing
│   │   │   ├── llm.py       # Enhanced Groq LLM integration
│   │   │   ├── document.py  # DOCX/PPTX generation with templates
│   │   │   └── image.py     # Pexels API integration
│   │   ├── schemas/         # Pydantic request/response schemas
│   │   │   ├── user.py      # User validation schemas
│   │   │   └── project.py   # Project/section schemas
│   │   ├── config.py        # Environment configuration
│   │   └── database.py      # SQLAlchemy setup
│   ├── main.py              # FastAPI application entry
│   ├── migrate_db.py        # Database migration script
│   ├── show_db.py           # Database inspection utility
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment variables (not in git)
│   └── presentwallah.db     # SQLite database (auto-created)
│
└── frontend/
    ├── src/
    │   ├── components/      # Reusable React components
    │   │   ├── ProtectedRoute.jsx  # Auth guard
    │   │   ├── SlidePreview.jsx    # Slide preview with images
    │   │   └── SlidePreview.css
    │   ├── contexts/        # React contexts
    │   │   └── AuthContext.jsx     # Authentication state
    │   ├── pages/           # Page components
    │   │   ├── Login.jsx           # Login page with animations
    │   │   ├── Register.jsx        # Registration page
    │   │   ├── Dashboard.jsx       # Project dashboard
    │   │   ├── CreateProject.jsx   # Project creation wizard
    │   │   ├── ProjectEditor.jsx   # Content editor
    │   │   ├── Auth.css           # Auth page styling
    │   │   ├── Dashboard.css      # Dashboard styling
    │   │   ├── CreateProject.css  # Project creation styling
    │   │   └── ProjectEditor.css  # Editor styling
    │   ├── services/        # API client
    │   │   └── api.js              # Axios configuration & API calls
    │   ├── App.jsx          # Main app component with routing
    │   ├── main.jsx         # React entry point
    │   └── index.css        # Global styles with animations
    ├── index.html           # HTML entry with Inter font
    ├── package.json         # NPM dependencies
    └── vite.config.js       # Vite configuration
```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Projects
- `GET /api/projects` - List all user projects
- `POST /api/projects` - Create new project
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project settings (template, font_size)
- `DELETE /api/projects/{id}` - Delete project
- `POST /api/projects/generate-content` - Generate AI content
- `POST /api/projects/refine-content` - Refine section content
- `PUT /api/projects/sections/{id}` - Update section feedback
- `POST /api/projects/ai-suggest` - Get AI outline suggestions
- `GET /api/projects/{id}/export` - Export document

## 🗄️ Database Schema

### Users
- `id`: Primary key
- `email`: Unique email address
- `username`: Unique username
- `hashed_password`: Bcrypt hashed password
- `created_at`: Timestamp

### Projects
- `id`: Primary key
- `title`: Project title
- `document_type`: ENUM (docx, pptx)
- `main_topic`: Main topic description
- `template`: Template style (modern/minimal/corporate/creative) - PowerPoint only
- `font_size`: Font size in points (default: 20) - PowerPoint only
- `user_id`: Foreign key to users
- `created_at`, `updated_at`: Timestamps

### Sections
- `id`: Primary key
- `project_id`: Foreign key to projects
- `title`: Section/slide title
- `content`: Generated/refined content
- `order`: Display order
- `liked`: Boolean feedback (True=👍, False=👎, NULL=no feedback) **[PERSISTED]**
- `comment`: User notes/comments **[PERSISTED]**
- `created_at`, `updated_at`: Timestamps

### Revisions (Complete Audit Trail)
- `id`: Primary key
- `section_id`: Foreign key to sections
- `prompt`: User's refinement instruction **[PERSISTED]**
- `previous_content`: Content before refinement **[PERSISTED]**
- `new_content`: Content after refinement **[PERSISTED]**
- `created_at`: Timestamp **[PERSISTED]**

**Note**: Every refinement creates a new revision record. Use `python show_db.py` to view complete history.

## 🧪 Testing

### Backend Testing
```powershell
cd backend
pytest
```

### Manual Testing Checklist
- [ ] User registration with validation
- [ ] User login and token generation
- [ ] Dashboard displays projects
- [ ] Create Word document project
- [ ] Create PowerPoint project
- [ ] AI outline suggestion works
- [ ] Manual section creation/reordering
- [ ] Content generation for all sections
- [ ] Content refinement with AI
- [ ] Like/Dislike feedback persists
- [ ] Comments save properly
- [ ] Document export (.docx)
- [ ] Document export (.pptx)
- [ ] Project deletion

## 🚨 Troubleshooting

### Backend Issues

**Database errors**:
```powershell
# Delete the database and restart
rm presentwallah.db
uvicorn main:app --reload
```

**Module import errors**:
```powershell
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1
# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend Issues

**Dependencies errors**:
```powershell
# Clear node modules and reinstall
rm -r node_modules
rm package-lock.json
npm install
```

**API connection issues**:
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Verify proxy configuration in `frontend/vite.config.js`

### Common Issues

**Groq API errors**:
- Verify your API key is correct in `.env`
- Check API rate limits
- Ensure you have sufficient credits

**Token expiration**:
- Login again to get a new token
- Adjust `ACCESS_TOKEN_EXPIRE_MINUTES` in `.env` if needed

## 🔒 Security Considerations

- **Passwords**: Hashed using bcrypt before storage
- **JWT Tokens**: Stored in localStorage, transmitted via Authorization header
- **API Keys**: Never exposed to frontend, stored in backend `.env`
- **CORS**: Configured to allow only development origins
- **SQL Injection**: Prevented by SQLAlchemy ORM parameterization

## 🚀 Deployment

### Backend Deployment (Railway/Render/Heroku)

1. **Prepare for deployment**:
   ```bash
   # Ensure requirements.txt is up to date
   pip freeze > requirements.txt
   ```

2. **Set environment variables** in your hosting platform:
   ```
   SECRET_KEY=<generate-strong-random-key>
   GROQ_API_KEY=<your-groq-key>
   PEXELS_API_KEY=<your-pexels-key>
   DATABASE_URL=<postgresql-url-if-using-postgres>
   ```

3. **For PostgreSQL** (recommended for production):
   - Update DATABASE_URL to PostgreSQL connection string
   - Ensure SQLAlchemy models are compatible

4. **Configure CORS**:
   - Update `allow_origins` in `backend/main.py` with your frontend URL

5. **Run migrations**:
   ```bash
   python migrate_db.py
   ```

### Frontend Deployment (Vercel/Netlify)

1. **Update API base URL**:
   - Edit `src/services/api.js`
   - Change `baseURL` to your deployed backend URL

2. **Build the application**:
   ```bash
   npm run build
   ```

3. **Deploy the `dist` folder** to your hosting platform

4. **Configure build settings** (for Vercel/Netlify):
   - Build command: `npm run build`
   - Output directory: `dist`
   - Node version: 18.x or higher

### Example Deployment Commands

**Backend (Railway)**:
```bash
railway login
railway init
railway add
railway up
```

**Frontend (Vercel)**:
```bash
npm install -g vercel
vercel login
vercel --prod
```

## 📝 Future Enhancements

- [ ] Rich text editor for manual content editing
- [ ] Multiple LLM provider support (OpenAI, Anthropic, etc.)
- [ ] Collaborative editing with real-time sync
- [ ] Custom template builder with color picker
- [ ] Per-slide template override
- [ ] Font family selection (beyond size)
- [ ] Version control UI for browsing revisions
- [ ] Export to PDF format
- [ ] Real-time AI suggestions while typing
- [ ] Document styling customization (margins, spacing)
- [ ] Bulk operations (template changes, exports)
- [ ] Team workspaces and sharing
- [ ] AI chat interface for content discussion
- [ ] Integration with Google Drive/Dropbox
- [ ] Custom branding/themes per user


## 🎯 Usage Examples

### Example 1: Creating a Business Strategy Presentation

1. Create new PowerPoint project
2. Title: "Q4 Marketing Strategy"
3. Topic: "Comprehensive digital marketing strategy for Q4 2024 targeting Gen-Z consumers"
4. Select **Corporate** template, font size 20pt
5. Click "AI-Suggest Outline" → Get 8 professional slide titles
6. Generate content → AI creates executive-level bullet points with metrics
7. Refine slide 3: "Add specific social media platforms and engagement metrics"
8. Export → Professional presentation with corporate theme and stock images

### Example 2: Creating a Technical Report

1. Create new Word document project  
2. Title: "Cloud Migration Assessment"
3. Topic: "Technical and financial assessment of migrating legacy systems to AWS cloud infrastructure"
4. Manually add sections: Executive Summary, Current Architecture, Proposed Architecture, Cost Analysis, Risk Assessment, Timeline, Recommendations
5. Generate content → AI creates 300-500 word sections with technical depth
6. Refine "Cost Analysis": "Include TCO comparison and ROI projections"
7. Add comments to specific sections for internal review
8. Export → Professional Word document ready for stakeholders

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Development Guidelines:**
- Follow existing code style and patterns
- Add comments for complex logic
- Update README.md if adding new features
- Test thoroughly before submitting PR



## 👤 Author

**Ankush Mitra**
- GitHub: [@ankurious](https://github.com/ankurious)
- Email: ankush.mitra4u@gmail.com

## 🙏 Acknowledgments

- **FastAPI** - Modern, fast web framework for Python
- **Groq** - Lightning-fast LLM inference with llama-3.3-70b-versatile
- **React** - Powerful UI library with excellent developer experience
- **Vite** - Next-generation frontend build tool
- **python-docx** & **python-pptx** - Python libraries for Office document generation
- **Pexels** - High-quality free stock photos
- **SQLAlchemy** - Robust Python SQL toolkit and ORM
- **Inter Font** - Beautiful open-source typeface by Rasmus Andersson

## 📞 Support

If you encounter any issues or have questions:


1. Review existing documentation
2. Open an issue on GitHub
3. Contact: ankush.mitra4u@gmail.com

---

**Note**: This application is designed for educational and demonstration purposes. For production deployment, ensure:
- Strong SECRET_KEY generation
- HTTPS/SSL configuration
- Rate limiting on API endpoints
- Input validation and sanitization
- Regular security audits
- Proper error logging and monitoring
- Database backups

---

Made with ❤️ by Ankush Mitra | **PresentWallah** - AI-Powered Document Creation
