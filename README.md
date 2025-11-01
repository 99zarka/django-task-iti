# Django Task ITI - Day 6

This project is a Django application developed as part of the ITI Day 6 tasks.

## Project Structure

- `api/`: Contains the Django REST Framework API for the application.
  - `models.py`: Defines the database models.
  - `serializers.py`: Defines the serializers for converting model instances to JSON and vice-versa.
  - `views.py`: Contains the viewsets for handling API requests.
  - `urls.py`: Defines the URL routing for the API.
  - `permissions.py`: Custom permission classes.
- `djan_project/`: The main Django project configuration.
  - `settings.py`: Project settings.
  - `urls.py`: Main URL dispatcher.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: Lists project dependencies.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/99zarka/django-task-iti.git
   cd django-task-iti
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

(Add specific API endpoints and their usage here, e.g., for tasks, users, etc.)

## Contributing

Feel free to contribute to this project. Please create a new branch for your features or bug fixes and submit a pull request.
