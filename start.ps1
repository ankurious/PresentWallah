# OceanAI Startup Script
# This script starts both backend and frontend servers

Write-Host "Starting OceanAI Platform..." -ForegroundColor Cyan
Write-Host ""

# Check if .env exists in backend
if (-not (Test-Path "backend\.env")) {
    Write-Host "[WARNING] backend\.env file not found!" -ForegroundColor Yellow
    Write-Host "Please create backend\.env file with your GROQ_API_KEY" -ForegroundColor Yellow
    Write-Host "You can copy from backend\.env.example" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        exit
    }
}

# Start Backend
Write-Host "[Starting Backend Server...]" -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\Activate.ps1; uvicorn main:app --reload --host 0.0.0.0 --port 8000"

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "[Starting Frontend Server...]" -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host ""
Write-Host "[OK] Both servers are starting..." -ForegroundColor Green
Write-Host ""
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to stop all servers..." -ForegroundColor Yellow

# Wait for user input to close
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Kill all related processes
Write-Host "Stopping servers..." -ForegroundColor Red
Stop-Process -Name "uvicorn" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "node" -Force -ErrorAction SilentlyContinue
