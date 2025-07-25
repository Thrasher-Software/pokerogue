@echo off
setlocal enabledelayedexpansion

echo ========================================
echo     PokéRogue Launcher for Windows
echo ========================================
echo.

REM Check if Git is installed
echo [1/8] Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH.
    echo Please install Git from https://git-scm.com/download/win
    pause
    exit /b 1
)
echo ✓ Git is installed

REM Check if Node.js is installed
echo [2/8] Checking if Node.js is installed...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH.
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
echo ✓ Node.js is installed

REM Check Node.js version (requires 22.0.0 or higher)
for /f "tokens=*" %%i in ('node --version') do set NODE_VERSION=%%i
echo   Node.js version: %NODE_VERSION%

REM Attempt to cd into pokerogue directory
echo [3/8] Looking for pokerogue directory...
if exist "pokerogue" (
    echo ✓ Found pokerogue directory
    cd pokerogue
) else (
    echo ⚠ pokerogue directory not found
    echo.
    set /p CLONE_CHOICE="Would you like to download PokéRogue? (y/n): "
    if /i "!CLONE_CHOICE!"=="y" (
        echo Cloning PokéRogue repository...
        git clone https://github.com/Thrasher-Software/pokerogue.git
        if %errorlevel% neq 0 (
            echo ERROR: Failed to clone repository
            pause
            exit /b 1
        )
        cd pokerogue
    ) else (
        echo Repository not cloned. Exiting...
        pause
        exit /b 1
    )
)

REM Git fetch to check for updates
echo [4/8] Checking for updates...
git fetch origin
if %errorlevel% neq 0 (
    echo WARNING: Failed to fetch updates from origin
)

REM Check if there are updates available
for /f %%i in ('git rev-list HEAD..origin/main --count 2^>nul') do set UPDATE_COUNT=%%i
if "%UPDATE_COUNT%"=="" set UPDATE_COUNT=0

if %UPDATE_COUNT% gtr 0 (
    echo [5/8] %UPDATE_COUNT% update(s) available
    set /p UPDATE_CHOICE="Would you like to download the latest updates? (y/n): "
    if /i "!UPDATE_CHOICE!"=="y" (
        echo Downloading updates...
        git pull origin main
        if %errorlevel% neq 0 (
            echo WARNING: Failed to pull updates
        ) else (
            echo ✓ Updates downloaded successfully
        )
    ) else (
        echo Skipping updates
    )
) else (
    echo [5/8] ✓ Already up to date
)

REM Install/update dependencies
echo [6/8] Installing dependencies...
npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Start the development server
echo [7/8] Starting PokéRogue development server...
echo.
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop the server
echo.

REM Start the server in background and capture its PID
start /b npm run start:dev
set SERVER_PID=%!

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

REM Launch browser
echo [8/8] Opening browser...
start http://localhost:8000

REM Create a temporary VBS script to monitor browser
echo Set objWMIService = GetObject("winmgmts:\\.\root\cimv2") > monitor_browser.vbs
echo Set colProcesses = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name = 'chrome.exe' OR Name = 'firefox.exe' OR Name = 'msedge.exe' OR Name = 'iexplore.exe' OR Name = 'opera.exe'") >> monitor_browser.vbs
echo If colProcesses.Count = 0 Then >> monitor_browser.vbs
echo     WScript.Echo "no_browser" >> monitor_browser.vbs
echo Else >> monitor_browser.vbs
echo     WScript.Echo "browser_running" >> monitor_browser.vbs
echo End If >> monitor_browser.vbs

echo.
echo ========================================
echo   PokéRogue is now running!
echo   Browser: http://localhost:8000
echo   Press any key to stop the server
echo ========================================
echo.

REM Wait for user input to stop
pause >nul

REM Kill the server process
echo.
echo Stopping development server...
taskkill /f /im node.exe >nul 2>&1
taskkill /f /im npm.exe >nul 2>&1

REM Clean up temporary files
if exist monitor_browser.vbs del monitor_browser.vbs

echo Server stopped. Goodbye!
pause
