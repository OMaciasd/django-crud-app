# My Project

This is an example project to demonstrate a Django web application with PostgreSQL.

## Requirements

- Python 3.x
- PostgreSQL

## Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
  ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
  ```
4. Create the database tables:
   ```bash
   python manage.py migrate
  ```

5. Create the database tables:
   ```bash
   python manage.py runserver
  ```
