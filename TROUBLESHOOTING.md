# 🔧 PresentWallah Troubleshooting Guide

## Common Issues and Solutions

---

## 🚀 Startup Issues

### Issue: "Command not found: python"
**Solution:**
```powershell
# Try python3 instead
python3 --version

# Or install Python from python.org
```

### Issue: "Command not found: npm"
**Solution:**
- Install Node.js from https://nodejs.org
- Restart your terminal after installation

### Issue: Virtual environment activation fails
**Solution:**
```powershell
# Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.\venv\Scripts\Activate.ps1
```

---

## 📦 Installation Issues

### Issue: pip install fails with "Permission denied"
**Solution:**
```powershell
# Use --user flag
pip install --user -r requirements.txt

# Or run as administrator
```

### Issue: "No module named 'app'"
**Solution:**
```powershell
# Make sure you're in the backend directory
cd backend

# Verify __init__.py files exist
ls app\__init__.py
```

### Issue: npm install fails
**Solution:**
```powershell
# Clear npm cache
npm cache clean --force

# Delete node_modules and try again
rm -r node_modules
rm package-lock.json
npm install
```

---

## 🔑 API Key Issues

### Issue: "Invalid API key" error
**Symptoms:**
- Error when generating content
- 401 Unauthorized errors

**Solutions:**
1. Check your .env file:
   ```powershell
   cat backend\.env
   ```

2. Verify the key format:
   - Should start with `gsk_`
   - No spaces before/after
   - No quotes around the key

3. Test the API key:
   ```python
   from groq import Groq
   client = Groq(api_key="your-key-here")
   # Should not error
   ```

### Issue: "GROQ_API_KEY not set"
**Solution:**
```powershell
# Check if .env exists
ls backend\.env

# If not, create it from example
cp backend\.env.example backend\.env

# Edit and add your key
notepad backend\.env
```

---

## 🗄️ Database Issues

### Issue: "database is locked"
**Solution:**
```powershell
# Close any open database connections
# Stop the backend server
# Delete and recreate database
cd backend
rm presentwallah.db
uvicorn main:app --reload
```

### Issue: "no such table: users"
**Solution:**
```powershell
# Delete database to recreate tables
rm backend\oceanai.db

# Restart backend (tables auto-create)
cd backend
uvicorn main:app --reload
```

### Issue: Migration errors
**Solution:**
```powershell
# Fresh start
rm backend\oceanai.db

# Tables will be created automatically on first run
```

---

## 🌐 Network Issues

### Issue: "Failed to fetch" / CORS errors
**Symptoms:**
- Browser console shows CORS errors
- API requests fail from frontend

**Solutions:**
1. Verify backend is running on port 8000:
   ```powershell
   curl http://localhost:8000/health
   ```

2. Check CORS settings in `backend/main.py`:
   ```python
   allow_origins=["http://localhost:3000", "http://localhost:5173"]
   ```

3. Clear browser cache and cookies

### Issue: "Port already in use"
**Solution:**
```powershell
# Find and kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
uvicorn main:app --reload --port 8001
```

---

## 🔐 Authentication Issues

### Issue: "Could not validate credentials"
**Symptoms:**
- Logged in but requests fail
- Token expired message

**Solutions:**
1. Login again to get fresh token

2. Check token in localStorage:
   - Open browser DevTools
   - Application → Local Storage
   - Verify token exists

3. Increase token expiry time in `.env`:
   ```env
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

### Issue: Can't register - "Email already registered"
**Solution:**
```powershell
# Use different email or clear database
rm backend\oceanai.db
```

### Issue: Password validation fails
**Solution:**
- Password must be at least 6 characters
- Check for special characters if issues persist

---

## 🤖 AI Generation Issues

### Issue: Content generation is very slow
**Possible causes:**
- Network latency
- Groq API rate limits
- Large number of sections

**Solutions:**
1. Check your internet connection

2. Reduce number of sections (test with 3-4)

3. Wait between generations:
   - Don't click "Generate" multiple times

4. Check Groq API status:
   - Visit https://status.groq.com

### Issue: Generated content is generic
**Solution:**
1. Make your main topic more specific:
   - Bad: "Business Report"
   - Good: "Q4 2025 Financial Performance Analysis for Tech Startup"

2. Use refinement feature:
   - "Add specific statistics"
   - "Include industry trends"
   - "Make more technical"

### Issue: Refinement not working
**Solutions:**
1. Verify section has content first

2. Be specific in refinement prompt:
   - Bad: "Make it better"
   - Good: "Convert to bullet points and add metrics"

3. Check API key and rate limits

---

## 📄 Export Issues

### Issue: Downloaded file won't open
**Symptoms:**
- Word/PowerPoint says file is corrupted
- File size is 0 bytes

**Solutions:**
1. Ensure content was generated:
   - All sections should have text
   - Don't export empty project

2. Check browser console for errors

3. Try different browser

4. Verify python-docx and python-pptx installed:
   ```powershell
   pip list | findstr docx
   pip list | findstr pptx
   ```

### Issue: Export button doesn't respond
**Solutions:**
1. Open browser console (F12)
2. Look for JavaScript errors
3. Check network tab for failed requests
4. Ensure backend is running

### Issue: Formatting is wrong in exported file
**Known limitations:**
- Basic formatting only
- No custom styles
- Standard templates used

**To customize:**
- Edit the downloaded file in Word/PowerPoint
- Modify `backend/app/services/document.py` for different templates

---

## 🎨 Frontend Issues

### Issue: Page is blank / white screen
**Solutions:**
1. Check browser console for errors (F12)

2. Verify React is running:
   ```powershell
   cd frontend
   npm run dev
   ```

3. Clear browser cache:
   - Ctrl + Shift + Delete
   - Clear all

4. Try different browser

### Issue: Styles not loading
**Solution:**
```powershell
# Rebuild
cd frontend
npm run build
npm run dev
```

### Issue: Changes not reflecting
**Solution:**
1. Hard refresh: Ctrl + F5

2. Restart Vite:
   ```powershell
   # In frontend terminal
   Ctrl + C
   npm run dev
   ```

---

## 🐛 Debugging Tips

### Enable Debug Mode

**Backend:**
```python
# In main.py
app = FastAPI(debug=True)
```

**Frontend:**
```javascript
// In components, add console.logs
console.log('Data:', data);
```

### Check Logs

**Backend logs:**
- Look at terminal running uvicorn
- Errors appear in red

**Frontend logs:**
- Browser console (F12)
- Network tab for API calls

### Test API Directly

**Using curl:**
```powershell
# Test health endpoint
curl http://localhost:8000/health

# Test login
curl -X POST http://localhost:8000/api/auth/login `
  -H "Content-Type: application/x-www-form-urlencoded" `
  -d "username=testuser&password=test123"
```

**Using browser:**
- Visit http://localhost:8000/docs
- Interactive API documentation
- Test endpoints directly

---

## 🔍 Diagnostic Commands

### Check System

```powershell
# Python version
python --version

# Node version
node --version

# npm version
npm --version

# Check if ports are in use
netstat -ano | findstr :8000
netstat -ano | findstr :3000
```

### Check Backend

```powershell
cd backend

# Virtual environment activated?
where python
# Should show path in venv

# Packages installed?
pip list

# Database exists?
ls presentwallah.db

# Environment file?
cat .env
```

### Check Frontend

```powershell
cd frontend

# Dependencies installed?
ls node_modules

# Build working?
npm run build
```

---

## 🆘 Emergency Reset

If nothing works, nuclear option:

```powershell
# 1. Stop all servers
# Press Ctrl+C in terminals

# 2. Clean everything
cd backend
rm -r venv
rm presentwallah.db
cd ..

cd frontend
rm -r node_modules
rm package-lock.json
cd ..

# 3. Fresh setup
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..

cd frontend
npm install
cd ..

# 4. Configure .env
# Add your GROQ_API_KEY to backend/.env

# 5. Start fresh
# Terminal 1
cd backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload

# Terminal 2
cd frontend
npm run dev
```

---

## 📞 Getting Help

### Before Asking for Help

Provide:
1. **What you're trying to do**
2. **What you expected**
3. **What actually happened**
4. **Error messages** (full text)
5. **Your environment**:
   - OS version
   - Python version
   - Node version
   - Browser

### Where to Find Help

1. **Check logs first**
   - Backend terminal
   - Browser console

2. **Review documentation**
   - README.md
   - QUICKSTART.md
   - This file

3. **Search error messages**
   - Google the exact error
   - Check Stack Overflow

4. **API documentation**
   - FastAPI: https://fastapi.tiangolo.com
   - React: https://react.dev
   - Groq: https://console.groq.com/docs

---

## ✅ Health Check Script

Create `check.ps1` to verify everything:

```powershell
Write-Host "🔍 PresentWallah Health Check" -ForegroundColor Cyan

# Check Python
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "✅ Python installed" -ForegroundColor Green
} else {
    Write-Host "❌ Python not found" -ForegroundColor Red
}

# Check Node
if (Get-Command node -ErrorAction SilentlyContinue) {
    Write-Host "✅ Node.js installed" -ForegroundColor Green
} else {
    Write-Host "❌ Node.js not found" -ForegroundColor Red
}

# Check backend files
if (Test-Path "backend\main.py") {
    Write-Host "✅ Backend files present" -ForegroundColor Green
} else {
    Write-Host "❌ Backend files missing" -ForegroundColor Red
}

# Check frontend files
if (Test-Path "frontend\package.json") {
    Write-Host "✅ Frontend files present" -ForegroundColor Green
} else {
    Write-Host "❌ Frontend files missing" -ForegroundColor Red
}

# Check .env
if (Test-Path "backend\.env") {
    Write-Host "✅ .env file exists" -ForegroundColor Green
} else {
    Write-Host "⚠️  .env file missing" -ForegroundColor Yellow
}

Write-Host "`nHealth check complete!" -ForegroundColor Cyan
```

---

**Remember:** Most issues are solved by:
1. Restarting servers
2. Checking .env configuration
3. Verifying API key
4. Clearing browser cache
5. Reading error messages carefully
