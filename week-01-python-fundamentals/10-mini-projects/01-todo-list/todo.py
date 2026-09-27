# ==========================================================
# Mini Project 1 - To-Do List
# ==========================================================
#
# THEORY:
#
# A To-Do List application allows users to create and manage
# tasks.
#
# In this version, tasks are stored in a Python list while the
# program is running.
#
# This project practices:
#
# - Lists
# - Dictionaries
# - Functions
# - Loops
# - Conditions
# - User input
# - Basic exception handling
#
# NOTE:
# Data will be lost when the program exits because we are not
# using a file/database yet.
#
# ==========================================================


tasks = []


# ----------------------------------------------------------
# Create
# ----------------------------------------------------------

def add_task() -> None:
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully.")


# ----------------------------------------------------------
# Read
# ----------------------------------------------------------

def view_tasks() -> None:
    if not tasks:
        print("No tasks available.")
        return

    print("\nTask List:")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(
            f'{task["id"]}. {task["title"]} - {status}'
        )


# ----------------------------------------------------------
# Update
# ----------------------------------------------------------

def complete_task() -> None:
    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


# ----------------------------------------------------------
# Delete
# ----------------------------------------------------------

def delete_task() -> None:
    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


# ----------------------------------------------------------
# Main application
# ----------------------------------------------------------

def main() -> None:

    while True:

        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()