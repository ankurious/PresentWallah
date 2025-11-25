# OceanAI - First Time Setup Script
# Run this script once to set up the entire project

Write-Host "OceanAI - First Time Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit
}

# Check Node.js
Write-Host "Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "[OK] Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Node.js not found! Please install Node.js 16+" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setting up Backend..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Backend setup
cd backend

Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
python -m venv venv

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Create .env if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "[IMPORTANT] Please edit backend\.env and add your GROQ_API_KEY!" -ForegroundColor Red
} else {
    Write-Host "[OK] .env file already exists" -ForegroundColor Green
}

cd ..

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setting up Frontend..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Frontend setup
cd frontend

Write-Host "Installing Node.js dependencies..." -ForegroundColor Yellow
npm install

cd ..

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Edit backend\.env and add your GROQ_API_KEY" -ForegroundColor Yellow
Write-Host "   Get a free key from: https://console.groq.com" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Run the application:" -ForegroundColor Yellow
Write-Host "   .\start.ps1" -ForegroundColor White
Write-Host ""
Write-Host "Or start manually:" -ForegroundColor Yellow
Write-Host "   Terminal 1: cd backend; .\venv\Scripts\Activate.ps1; uvicorn main:app --reload" -ForegroundColor White
Write-Host "   Terminal 2: cd frontend; npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "Read README.md for detailed documentation" -ForegroundColor Cyan
Write-Host ""
