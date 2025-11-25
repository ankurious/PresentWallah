# 🚀 PresentWallah - Quick Reference Card

## ⚡ Quick Start Commands

### First Time Setup
```powershell
# Run the setup script
.\setup.ps1
```

### Start Application
```powershell
# Option 1: Use startup script
.\start.ps1

# Option 2: Manual start
# Terminal 1 (Backend)
cd backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload

# Terminal 2 (Frontend)
cd frontend
npm run dev
```

---

## 📍 Important URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| Groq Console | https://console.groq.com |

---

## 📁 Project Structure

```
PresentWallah/
├── backend/          → FastAPI server
│   ├── app/
│   │   ├── models/   → Database models
│   │   ├── routers/  → API endpoints
│   │   ├── services/ → Business logic
│   │   └── schemas/  → Data validation
│   ├── main.py       → App entry
│   └── .env          → Config (create this!)
│
└── frontend/         → React app
    ├── src/
    │   ├── pages/    → Main pages
    │   ├── contexts/ → State management
    │   └── services/ → API calls
    └── package.json
```

---

## 🔑 Environment Variables

**backend/.env** (Required):
```env
GROQ_API_KEY=gsk_your_key_here  # 👈 MUST SET THIS!
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Get Groq API key: https://console.groq.com/keys

---

## 🎯 User Flow

1. **Register** → Create account
2. **Login** → Authenticate
3. **Dashboard** → View projects
4. **Create Project** → Choose doc type
5. **Configure** → Add sections/slides
6. **Generate** → AI creates content
7. **Refine** → Improve with AI
8. **Export** → Download document

---

## 🤖 AI Features

### Content Generation
- Creates unique content per section
- Context-aware (topic + section title)
- Different styles for Word vs PowerPoint

### AI-Suggest Outline
- Enter topic only
- AI generates structure
- Edit before confirming

### Content Refinement
- "Make this more formal"
- "Add bullet points"
- "Shorten to 100 words"
- "Add statistics"

---

## 📝 Document Types

### Word (.docx)
- Sections with headers
- Paragraph content (200-400 words)
- Professional formatting

### PowerPoint (.pptx)
- Slides with titles
- Bullet points (3-6 per slide)
- Presentation format

---

## 🛠️ Common Commands

### Backend
```powershell
# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload

# Different port
uvicorn main:app --reload --port 8001

# Check packages
pip list
```

### Frontend
```powershell
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Clear cache
npm cache clean --force
```

### Database
```powershell
# Reset database
rm backend\oceanai.db

# Recreate (auto on start)
uvicorn main:app --reload
```

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| No API key error | Add GROQ_API_KEY to .env |
| Port in use | Change port or kill process |
| CORS error | Check backend is on 8000 |
| Database locked | Stop server, delete presentwallah.db |
| Can't activate venv | Run as admin, check ExecutionPolicy |
| npm errors | Delete node_modules, npm install |
| White screen | Check console, hard refresh |

---

## 📊 API Endpoints Reference

### Authentication
- POST `/api/auth/register` - Register user
- POST `/api/auth/login` - Login
- GET `/api/auth/me` - Get current user

### Projects
- GET `/api/projects` - List projects
- POST `/api/projects` - Create project
- GET `/api/projects/{id}` - Get details
- DELETE `/api/projects/{id}` - Delete

### Content
- POST `/api/projects/generate-content` - Generate all
- POST `/api/projects/refine-content` - Refine section
- POST `/api/projects/ai-suggest` - Suggest outline
- GET `/api/projects/{id}/export` - Export file

---

## 🎨 UI Components

### Pages
1. **Login** - User authentication
2. **Register** - New account
3. **Dashboard** - Project list
4. **CreateProject** - Project wizard
5. **ProjectEditor** - Content editor

### Features
- Like/Dislike buttons
- AI refinement input
- Comment boxes
- Section navigation
- Export button

---

## 🔐 Security Notes

- Passwords hashed with bcrypt
- JWT tokens (30 min expiry)
- Protected API endpoints
- CORS enabled for localhost
- .env not in Git

---

## 📦 Dependencies

### Backend (Python)
- fastapi - Web framework
- uvicorn - ASGI server
- sqlalchemy - ORM
- python-jose - JWT
- passlib - Password hashing
- python-docx - Word export
- python-pptx - PowerPoint export
- groq - LLM API

### Frontend (Node.js)
- react - UI framework
- react-router-dom - Routing
- axios - HTTP client
- vite - Build tool

---

## 🎓 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com
- **React**: https://react.dev
- **Groq API**: https://console.groq.com/docs
- **SQLAlchemy**: https://www.sqlalchemy.org

---

## 📞 Help

| Need Help With | Check File |
|----------------|------------|
| Installation | README.md |
| Quick setup | QUICKSTART.md |
| Issues | TROUBLESHOOTING.md |
| Testing | TESTING.md |
| Demo video | DEMO_SCRIPT.md |
| API key | GROQ_API_SETUP.md |

---

## ✅ Pre-Launch Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] Groq API key obtained
- [ ] .env file created
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Both servers running
- [ ] Browser opened to localhost:3000

---

## 🎯 Testing Scenarios

### Smoke Test (5 min)
1. Register new user
2. Create Word project
3. Generate content
4. Export .docx
5. Verify file opens

### Full Test (15 min)
1. All smoke test steps
2. Create PowerPoint project
3. Use AI-Suggest
4. Refine content
5. Add feedback/comments
6. Export .pptx
7. Test project deletion

---

## 🚨 Emergency Commands

```powershell
# Kill all processes
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# Fresh start
rm backend\oceanai.db
rm -r backend\venv
rm -r frontend\node_modules

# Run setup again
.\setup.ps1
```

---

## 💡 Pro Tips

1. **Use AI-Suggest** - Saves time on outlining
2. **Be specific** - Better topics = better content
3. **Refine iteratively** - Small changes at a time
4. **Save early** - Feedback auto-saves
5. **Test exports** - Check documents before sharing

---

## 📈 Performance Tips

- Generate 5-8 sections at a time (not 20+)
- Wait for generation to complete
- Close unused browser tabs
- Use modern browser (Chrome/Edge)
- Check Groq API rate limits

---

## 🎉 You're Ready!

Everything you need to run PresentWallah successfully. For detailed info, see the full documentation files.

**Happy document generating! 🌊**
