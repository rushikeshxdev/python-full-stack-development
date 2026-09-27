# ==========================================================
# Task Manager - Main Application
# ==========================================================
#
# THEORY:
#
# `main.py` acts as the entry point of the application.
#
# It handles:
# - User input
# - Menu display
# - Calling TaskManager methods
#
# Business logic is kept inside task_manager.py.
# File/JSON logic is kept inside storage.py.
#
# ==========================================================

from task_manager import TaskManager


def display_tasks(tasks: list[dict]) -> None:

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TASKS ==========")

    for task in tasks:
        print(
            f'ID: {task["id"]} | '
            f'Title: {task["title"]} | '
            f'Status: {task["status"]}'
        )
        print(f'Description: {task["description"]}')
        print("-" * 40)


def main() -> None:

    manager = TaskManager()

    while True:

        print("\n========== TASK MANAGER ==========")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Find Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        # CREATE
        if choice == "1":

            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue

            task = manager.create_task(
                title,
                description
            )

            print(
                f"Task created successfully with ID {task.id}."
            )

        # READ ALL
        elif choice == "2":

            tasks = manager.get_tasks()

            display_tasks(tasks)

        # READ ONE
        elif choice == "3":

            try:
                task_id = int(input("Enter task ID: "))

                task = manager.get_task_by_id(task_id)

                if task:
                    print("\nTask found:")
                    print("ID:", task["id"])
                    print("Title:", task["title"])
                    print("Description:", task["description"])
                    print("Status:", task["status"])

                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid task ID.")

        # UPDATE
        elif choice == "4":

            try:
                task_id = int(input("Enter task ID to update: "))

                task = manager.get_task_by_id(task_id)

                if task is None:
                    print("Task not found.")
                    continue

                print("Press Enter to keep the current value.")

                title = input(
                    f'Title [{task["title"]}]: '
                ).strip()

                description = input(
                    f'Description [{task["description"]}]: '
                ).strip()

                status = input(
                    f'Status [{task["status"]}]: '
                ).strip()

                updated = manager.update_task(
                    task_id,
                    title or None,
                    description or None,
                    status or None
                )

                if updated:
                    print("Task updated successfully.")

            except ValueError:
                print("Please enter a valid task ID.")

        # DELETE
        elif choice == "5":

            try:
                task_id = int(input("Enter task ID to delete: "))

                deleted = manager.delete_task(task_id)

                if deleted:
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid task ID.")

        # EXIT
        elif choice == "6":

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()