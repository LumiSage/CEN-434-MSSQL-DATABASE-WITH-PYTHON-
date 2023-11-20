import pyodbc

def connect_to_database():
    conx_string = "driver={SQL Server}; server=DESKTOP-TE993MT\\MICROSOFTSQLSV; database=Helloworld; Trusted_Connection=yes;"
    return pyodbc.connect(conx_string)

def insert_student():
    name = input("Name: ")
    matno = input("Matno:")
    roomno = input("Roomno:")
    query = f"INSERT INTO table_name (Name_, matno, room) VALUES('{name}','{matno}','{roomno}')"
    with connect_to_database() as conx:
        cursor = conx.cursor()
        cursor.execute(query)
        conx.commit()
        print("Student added successfully.\n")

def select_all_students():
    query = "SELECT * FROM table_name"
    with connect_to_database() as conx:
        cursor = conx.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for item in data:
            print(" ".join(map(str, item)))
        print("Successfully fetched results\n")

def find_student():
    search_term = input("Enter name, matno, or roomno to search: ")
    query = f"SELECT * FROM table_name WHERE Name_ LIKE '%{search_term}%' OR matno LIKE '%{search_term}%' OR room LIKE '%{search_term}%'"
    with connect_to_database() as conx:
        cursor = conx.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for item in data:
            print(" ".join(map(str, item)))
        print("Search complete.\n")

def delete_student():
    matno = input("Enter Matno of student to delete: ")
    confirm = input(f"Are you sure you want to delete the student with Matno {matno}? (yes/no): ")
    if confirm.lower() == "yes":
        query = f"DELETE FROM table_name WHERE matno = '{matno}'"
        with connect_to_database() as conx:
            cursor = conx.cursor()
            cursor.execute(query)
            conx.commit()
            print("Student deleted successfully.\n")
    else:
        print("Deletion canceled.\n")

# Main loop
while True:
    print("1. List of All Students")
    print("2. Add New Student")
    print("3. Find a Student")
    print("4. Update Student Details")
    print("5. Delete Student from Log")
    print("6. End Program")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        select_all_students()
    elif choice == "2":
        insert_student()
    elif choice == "3":
        find_student()
    elif choice == "4":
        # Implement update student details
        pass
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
