# Django CRUD with Authentication and Login

## Overview
This is a Django-based web application that implements a CRUD (Create, Read, Update, Delete) functionality along with user authentication and login features. The project serves as a foundational structure for building web applications requiring user management and database interactions.

---

## Features
- User authentication (signup, login, logout).
- Create, read, update, and delete records in a database.
- Protected views that require user authentication.
- Responsive front-end design.
- Clear project structure for easy understanding and extensibility.

---

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default for Django)
- **Authentication**: Django's built-in authentication system

---

## Installation

### Prerequisites
- Python (>= 3.8 recommended)
- Pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alexis-Sanchez-B/django-crud-auth-login.git
   cd django-crud-auth-login
   
2. Create and activate a virtual environment (optional):
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Run database migrations:
python manage.py migrate

5.Start the development server:
python manage.py runserver

6.Open your browser and visit http://127.0.0.1:8000/.

Usage
Authentication
Sign Up: Create a new account.
Login: Access the application using valid credentials.
Logout: End the session securely.
CRUD Operations
Create: Add new records using forms.
Read: View existing records in a user-friendly table.
Update: Edit records through an intuitive interface.
Delete: Remove records with a confirmation prompt.

django-crud-auth-login/
│
├── crud_app/                # Main app handling CRUD operations
│   ├── migrations/          # Database migration files
│   ├── templates/           # HTML templates
│   ├── static/              # Static files (CSS, JS, images)
│   ├── views.py             # Application logic
│   ├── models.py            # Database models
│   ├── forms.py             # Form definitions
│   └── urls.py              # URL routes for the app
│
├── project/                 # Django project settings
│   ├── settings.py          # Main configuration file
│   ├── urls.py              # Project-level URL routes
│   └── wsgi.py              # WSGI application
│
├── db.sqlite3               # SQLite database file
├── manage.py                # Django management script
└── requirements.txt         # List of dependencies
