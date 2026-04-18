import sqlite3

# Database Connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    
    cursor.execute("INSERT INTO students(name, age, course) VALUES(?,?,?)",
                   (name, age, course))
    conn.commit()
    print("Student Added Successfully")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    print("\nStudent Records")
    print("----------------")
    for row in rows:
        print(row)

# Delete Student
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student Deleted Successfully")

# Update Student
def update_student():
    student_id = input("Enter Student ID to update: ")
    name = input("Enter New Name: ")
    age = input("Enter New Age: ")
    course = input("Enter New Course: ")
    
    cursor.execute("""
    UPDATE students 
    SET name=?, age=?, course=? 
    WHERE id=?
    """, (name, age, course, student_id))
    
    conn.commit()
    print("Student Updated Successfully")

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
        
    elif choice == "2":
        view_students()
        
    elif choice == "3":
        update_student()
        
    elif choice == "4":
        delete_student()
        
    elif choice == "5":
        print("Thank You")
        break
        
    else:
        print("Invalid Choice")
      
