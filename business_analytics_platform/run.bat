@echo off
title AI-Based Business Analytics Dashboard
echo ========================================================
echo   NexusBI: AI-Based Business Analytics Dashboard
echo   Final-Year College Capstone Project
echo ========================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting application with python...
    python app.py
) else (
    if exist "%USERPROFILE%\anaconda3\python.exe" (
        echo Starting application with Anaconda Python...
        "%USERPROFILE%\anaconda3\python.exe" app.py
    ) else (
        echo [ERROR] Python not found in PATH or standard Anaconda path!
        echo Please ensure Python is installed and accessible.
        pause
    )
)
pause
