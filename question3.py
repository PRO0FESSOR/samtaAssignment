import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Establishes a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host="",       # your MySQL host
            user="",    # your MySQL username
            password="" # your MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    """
    Creates a new database named 'school_db' if it does not exist.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
        print("Database created successfully")
    except Error as e:
        print(f"Error: {e}")

def create_table(connection):
    """
    Creates a table named 'students' in the 'school_db' database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("USE school_db")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            grade DECIMAL(5, 2) NOT NULL
        )
        """)
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_student(connection):
    """
    Inserts a new student record into the 'students' table.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("USE school_db")
        insert_query = """
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
        """
        student_data = ("Alice", "Smith", 18, 95.5)
        cursor.execute(insert_query, student_data)
        connection.commit()
        print("Student record inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def update_student_grade(connection):
    """
    Updates the grade of the student with the first name 'Alice'.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("USE school_db")
        update_query = """
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
        """
        cursor.execute(update_query, (97.0, "Alice"))
        connection.commit()
        print("Student grade updated successfully")
    except Error as e:
        print(f"Error: {e}")

def delete_student(connection):
    """
    Deletes the student record with the last name 'Smith'.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("USE school_db")
        delete_query = """
        DELETE FROM students
        WHERE last_name = %s
        """
        cursor.execute(delete_query, ("Smith",))
        connection.commit()
        print("Student record deleted successfully")
    except Error as e:
        print(f"Error: {e}")

def fetch_all_students(connection):
    """
    Fetches and displays all student records from the 'students' table.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("USE school_db")
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("Student Records:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def main():
    # Create a database connection
    connection = create_connection()
    if connection is None:
        return

    # Create database and table
    create_database(connection)
    create_table(connection)

    # # Perform database operations
    insert_student(connection)
    update_student_grade(connection)
    delete_student(connection)
    fetch_all_students(connection)

    # # Close the connection
    if connection.is_connected():
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
