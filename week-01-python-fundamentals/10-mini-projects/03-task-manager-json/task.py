# 4. `task.py`

# ==========================================================
# Task Manager - Task Model
# ==========================================================
#
# THEORY:
#
# A class is a blueprint used to create objects.
#
# Here, each Task object represents one task in our application.
#
# A task contains:
# - id
# - title
# - description
# - status
#
# The `to_dict()` method converts the Task object into a
# Python dictionary so that it can be saved as JSON.
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
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    def mark_completed(self) -> None:
        self.status = "completed"