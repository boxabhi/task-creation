# Django Application

This is a Django application designed to demonstrate a simple task management system. Follow the instructions below to set up and run the project locally.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (>= 3.8)
- pip (Python package manager)
- Virtualenv (optional but recommended)

---

## Installation

1. **Clone the Repository**

   ```bash
    git clone <repository-url>
    cd <repository-folder>
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    http://127.0.0.1:8000/
