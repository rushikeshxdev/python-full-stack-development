# ==========================================================
# Mini Project 2 - Student CRUD
# ==========================================================
#
# THEORY:
#
# CRUD stands for:
#
# C -> Create
# R -> Read
# U -> Update
# D -> Delete
#
# This application manages student records using a Python
# list containing dictionaries.
#
# Example student:
#
# {
#     "id": 1,
#     "name": "Rushikesh",
#     "age": 23,
#     "branch": "CSBS"
# }
#
# Concepts practiced:
#
# - List
# - Dictionary
# - Functions
# - Loops
# - Conditions
# - User input
# - CRUD
# - Exception handling
# - Type hints
#
# NOTE:
#
# Data is stored only in memory.
# When the program exits, the data is lost.
#
# ==========================================================


students: list[dict] = []


# ----------------------------------------------------------
# Create
# ----------------------------------------------------------

def add_student() -> None:
    try:
        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: "))
        branch = input("Enter student branch: ").strip()

        if not name or not branch:
            print("Name and branch cannot be empty.")
            return

        student = {
            "id": len(students) + 1,
            "name": name,
            "age": age,
            "branch": branch
        }

        students.append(student)

        print("Student added successfully.")

    except ValueError:
        print("Age must be a valid number.")


# ----------------------------------------------------------
# Read - All students
# ----------------------------------------------------------

def view_students() -> None:
    if not students:
        print("No students found.")
        return

    print("\n========== STUDENTS ==========")

    for student in students:
        print(
            f'ID: {student["id"]} | '
            f'Name: {student["name"]} | '
            f'Age: {student["age"]} | '
            f'Branch: {student["branch"]}'
        )


# ----------------------------------------------------------
# Read - One student
# ----------------------------------------------------------

def find_student() -> None:
    try:
        student_id = int(input("Enter student ID: "))

        for student in students:
            if student["id"] == student_id:
                print("\nStudent found:")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# ----------------------------------------------------------
# Update
# ----------------------------------------------------------

def update_student() -> None:
    try:
        student_id = int(input("Enter student ID to update: "))

        for student in students:
            if student["id"] == student_id:

                new_name = input(
                    f'Enter new name [{student["name"]}]: '
                ).strip()

                new_age = input(
                    f'Enter new age [{student["age"]}]: '
                ).strip()

                new_branch = input(
                    f'Enter new branch [{student["branch"]}]: '
                ).strip()

                if new_name:
                    student["name"] = new_name

                if new_age:
                    student["age"] = int(new_age)

                if new_branch:
                    student["branch"] = new_branch

                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid age or student ID.")


# ----------------------------------------------------------
# Delete
# ----------------------------------------------------------

def delete_student() -> None:
    try:
        student_id = int(input("Enter student ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# ----------------------------------------------------------
# Main menu
# ----------------------------------------------------------

def main() -> None:

    while True:

        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            find_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()