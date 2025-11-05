import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "dbname": "Assignment3",  # your database name
    "user": "postgres",  # your database user
    "password": "admin",  # your database password
    "port": 5432
}


def connect_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    print("Database Connected")
    return conn, cur


def init_db(cur):
    cur.execute("""
                CREATE TABLE if not exists students (
                student_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name  TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                enrollment_date DATE
                );
                """)
    
    cur.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    cur.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                """)

    print("Database Default Records Initialized")

def close_db(conn, cur):
    cur.close()
    conn.close()
    print("Database Connection Closed")

def view_all_students(cur):
    cur.execute("""
                SELECT * FROM students
                ORDER BY student_id ASC;
                """)
    students = cur.fetchall()
    print("All Students:")
    
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Email: {student[3]}, Enrollment Date: {student[4]}")

def add_student(cur):
    first_name = input("Enter First Name: ")
    last_name =  input("Enter Last Name: ")
    email = input("Enter Email: ")
    enrollment_date = input("Enter Enrollment Date (YYYY-MM-DD): ")

    cur.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);
                """, (first_name, last_name, email, enrollment_date))
    print("Student added.")

def update_student_email(cur):
    student_id = input("Enter Student ID to Update: ")
    new_email = input("Enter New Email: ")
    cur.execute("""
                UPDATE students SET email = %s WHERE student_id = %s;
                """, (new_email, student_id))
    print("Student email updated.")

def delete_student(cur):
    student_id = input("Enter Student ID to Delete: ")
    cur.execute("""
                DELETE FROM students WHERE student_id = %s;
                """, (student_id,))
    print("Student deleted.")

if __name__ == "__main__":
    conn, cur = connect_db()
    init_db(cur)
    
    print("Select which operation to perform:")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Update Student Email")
    print("4. Delete Student")
    print("5. Exit")

    input_choice = 0
    while input_choice != "5":
        input_choice = input("Enter choice (1-5): ")
        if input_choice == "1":
            view_all_students(cur)
        elif input_choice == "2":
            add_student(cur)
        elif input_choice == "3":
            update_student_email(cur)
        elif input_choice == "4":
            delete_student(cur)
        elif input_choice == "5":
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")

    close_db(conn, cur)
   
