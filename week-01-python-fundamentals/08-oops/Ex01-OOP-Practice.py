# ==========================================================
# OOP Practice - Task
# ==========================================================
#
# PURPOSE:
#
# Build a simple Task class and practice:
# - Class
# - Object
# - Constructor
# - Attributes
# - Methods
# - Encapsulation
#
# This prepares us for the final JSON Task Manager.
#
# ==========================================================


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        status: str = "pending"
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.__status = status

    def mark_completed(self) -> None:
        self.__status = "completed"

    def get_status(self) -> str:
        return self.__status

    def display(self) -> None:
        print("ID:", self.id)
        print("Title:", self.title)
        print("Description:", self.description)
        print("Status:", self.__status)


# Create objects

task1 = Task(
    1,
    "Learn Python",
    "Complete Python fundamentals"
)

task2 = Task(
    2,
    "Learn OOP",
    "Understand classes and objects"
)


# Display tasks

task1.display()

print()

task2.display()


# Update task status

task1.mark_completed()

print("\nAfter completing Task 1:")

task1.display()