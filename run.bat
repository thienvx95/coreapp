@echo off
echo Starting StockAnalyze Application...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists and activate it
if exist "env\Scripts\activate.bat" (
    call env\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Creating one...
    python -m venv env
    call env\Scripts\activate.bat
)

REM Ensure pip is up to date and install requirements
echo Installing/updating dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Verify uvicorn is installed
uvicorn --version >nul 2>&1
if errorlevel 1 (
    echo Installing uvicorn...
    pip install uvicorn
)

REM Run the FastAPI application
echo Starting the server...
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

REM If the server stops, pause to see any error messages
pause 