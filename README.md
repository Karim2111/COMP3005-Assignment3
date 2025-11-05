# COMP3005-Assignment3: Karim Rifai 101300239
# Video Link:

## Setup Instructions
### Using Virtual Environment
1. Create venv
2. Activate venv
3. Install dependencies
```terminal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application
1. Ensure PostgreSQL server is running.
2. Update the database configuration in `main.py`
```python
DB_CONFIG = {
    "host": "localhost",
    "dbname": "Assignment3",  # your database name
    "user": "postgres",  # your database user
    "password": "admin",  # your database password
    "port": 5432
}
```
3. Run the application
```terminal
python main.py
```

## Application Features

### connect_db():
 - Connects to the PostgreSQL database using the provided configuration.

### init_db(cur):
 - Initializes the database and populating it with sample data.

### close_db(conn, cur):
 - Closes the database cursor and connection.

### view_all_students(cur):
 - Fetches and displays all student records

### add_student(cur):
 - Prompts the user for student details and inserts a new student record

### update_student_email(cur):
 - Prompts the user for a student ID and a new email, then updates the email of the specified student.

### delete_student(cur):
 - Prompts the user for a student ID and deletes the corresponding student record

### main loop:
 - Main app that provides a menu for users to interact with the database operations.
