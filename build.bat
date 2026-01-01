@echo off
REM Simple build script for Windows

echo ==========================================
echo Congruences Calculator - Build Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed!
    echo Please install Python 3 and try again.
    pause
    exit /b 1
)

echo ✓ Python found
python --version

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pip is not installed!
    echo Please install pip and try again.
    pause
    exit /b 1
)

echo ✓ pip found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo ✓ Dependencies installed
echo.

REM Build the executable
echo Building executable...
python build_exe.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Build failed!
    pause
    exit /b 1
)

echo.
echo ==========================================
echo ✓ Build completed successfully!
echo ==========================================
echo.
echo Your executable is located at: dist\CongruencesCalculator.exe
echo.
echo To run it, double-click: dist\CongruencesCalculator.exe
echo.
pause
