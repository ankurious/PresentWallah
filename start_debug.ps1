# OceanAI Debug Startup Script
Write-Host "Starting OceanAI Platform (Debug Mode)..." -ForegroundColor Cyan
Write-Host ""

# Start Backend in visible window
Write-Host "[Starting Backend Server...]" -ForegroundColor Green
$backendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'c:\Users\Ankush Mitra\Desktop\OceanAI\backend'; Write-Host 'Backend Server Starting...' -ForegroundColor Green; python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000" -PassThru

# Wait for backend to start
Start-Sleep -Seconds 4

# Start Frontend in visible window
Write-Host "[Starting Frontend Server...]" -ForegroundColor Green
$frontendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'c:\Users\Ankush Mitra\Desktop\OceanAI\frontend'; Write-Host 'Frontend Server Starting...' -ForegroundColor Green; npm run dev" -PassThru

Write-Host ""
Write-Host "[OK] Both servers are starting in separate windows..." -ForegroundColor Green
Write-Host ""
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend PID: $($backendJob.Id)" -ForegroundColor Yellow
Write-Host "Frontend PID: $($frontendJob.Id)" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press any key to stop all servers..." -ForegroundColor Yellow

# Wait for user input to close
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Kill specific processes
Write-Host "Stopping servers..." -ForegroundColor Red
Stop-Process -Id $backendJob.Id -Force -ErrorAction SilentlyContinue
Stop-Process -Id $frontendJob.Id -Force -ErrorAction SilentlyContinue

# Clean up any remaining processes
Get-Process | Where-Object {$_.ProcessName -like "*node*" -or $_.ProcessName -like "*python*"} | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "Servers stopped." -ForegroundColor Green
