# ==========================================================
# Task Manager - CRUD Logic
# ==========================================================
#
# THEORY:
#
# CRUD means:
#
# C -> Create
# R -> Read
# U -> Update
# D -> Delete
#
# This module contains the business logic for managing tasks.
#
# It gets data from storage.py and operates on it.
#
# ==========================================================

from task import Task
from storage import load_tasks, save_tasks


class TaskManager:

    def __init__(self):
        self.tasks = load_tasks()

    # ------------------------------------------------------
    # CREATE
    # ------------------------------------------------------

    def create_task(
        self,
        title: str,
        description: str
    ) -> Task:

        new_id = self._get_next_id()

        task = Task(
            new_id,
            title,
            description
        )

        self.tasks.append(task.to_dict())

        save_tasks(self.tasks)

        return task

    # ------------------------------------------------------
    # READ - ALL
    # ------------------------------------------------------

    def get_tasks(self) -> list[dict]:
        return self.tasks

    # ------------------------------------------------------
    # READ - ONE
    # ------------------------------------------------------

    def get_task_by_id(self, task_id: int) -> dict | None:

        for task in self.tasks:
            if task["id"] == task_id:
                return task

        return None

    # ------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None
    ) -> bool:

        task = self.get_task_by_id(task_id)

        if task is None:
            return False

        if title:
            task["title"] = title

        if description:
            task["description"] = description

        if status:
            task["status"] = status

        save_tasks(self.tasks)

        return True

    # ------------------------------------------------------
    # DELETE
    # ------------------------------------------------------

    def delete_task(self, task_id: int) -> bool:

        task = self.get_task_by_id(task_id)

        if task is None:
            return False

        self.tasks.remove(task)

        save_tasks(self.tasks)

        return True

    # ------------------------------------------------------
    # ID GENERATION
    # ------------------------------------------------------

    def _get_next_id(self) -> int:

        if not self.tasks:
            return 1

        return max(task["id"] for task in self.tasks) + 1