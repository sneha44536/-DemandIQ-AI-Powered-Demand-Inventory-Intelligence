@echo off

cd /d C:\Users\sneha\OneDrive\work\2

start "FastAPI Backend" cmd /k ".\venv\Scripts\python.exe -m uvicorn app.api:app --reload"

timeout /t 3 /nobreak >nul

start "Streamlit Frontend" cmd /k ".\venv\Scripts\python.exe -m streamlit run frontend\app.py"

timeout /t 5 /nobreak >nul

start http://localhost:8501

@echo off
cd /d C:\Users\sneha\OneDrive\work\2

call venv\Scripts\activate

start "" http://localhost:8501

streamlit run dashboard\dashboard.py