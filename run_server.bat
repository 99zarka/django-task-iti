@echo off
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists. Skipping creation.
)
echo Activating virtual environment...
call venv\Scripts\activate
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
echo Running Django server...
python manage.py runserver
pause
