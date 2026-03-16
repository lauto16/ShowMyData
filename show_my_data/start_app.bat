@echo off
start cmd /k "cd backend && call venv\Scripts\activate && uvicorn main:app --reload --port 5000"
start cmd /k "cd frontend\show-my-data && npm run dev"