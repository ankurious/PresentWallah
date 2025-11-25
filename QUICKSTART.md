# PresentWallah - Quick Start Guide

## Getting Started in 5 Minutes

### Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed
- A Groq API key (free at https://console.groq.com)

### Step 1: Clone & Setup Backend

```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "SECRET_KEY=your-secret-key-here
GROQ_API_KEY=your-groq-api-key-here" > .env

# Start backend
uvicorn main:app --reload
```

Backend running at: http://localhost:8000

### Step 2: Setup Frontend (New Terminal)

```powershell
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start frontend
npm run dev
```

Frontend running at: http://localhost:3000

### Step 3: Use the Application

1. Open http://localhost:3000
2. Register a new account
3. Login with your credentials
4. Create a new project
5. Generate AI content
6. Refine and export!

## Key Features to Try

1. **AI-Suggest Outline**: Let AI create the document structure
2. **Generate Content**: AI writes content for each section
3. **Refine Content**: Ask AI to modify specific sections
4. **Feedback**: Use like/dislike to track quality
5. **Export**: Download as .docx or .pptx

## Need Help?

- Backend API docs: http://localhost:8000/docs
- Check README.md for detailed documentation
- Verify .env has your Groq API key
