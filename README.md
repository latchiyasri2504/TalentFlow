# TalentFlow

AI-Powered Resume Parser & Multi-Channel 2FA Onboarding Pipeline

## Project Overview
TalentFlow is a backend application that simplifies student onboarding through resume parsing and OTP verification.

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- PDFPlumber
- JWT
- Argon2

## Features
- PDF and DOCX resume upload
- Resume data extraction
- User registration
- Password hashing
- OTP verification
- Student dashboard API

## Run the Project
python -m uvicorn app.main:app --reload

## API Documentation
http://127.0.0.1:8000/docs

## Current Status
Backend setup and database connection completed.
Registration API requires further debugging.
OTP delivery is currently simulated in the terminal.