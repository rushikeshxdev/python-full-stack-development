# ==========================================================
# Task Manager - JSON Storage
# ==========================================================
#
# THEORY:
#
# This module is responsible for storing and retrieving task
# data from the JSON file.
#
# Main responsibilities:
#
# - Load tasks from tasks.json
# - Save tasks to tasks.json
#
# We separate storage logic from CRUD logic so that each
# module has a clear responsibility.
#
# ==========================================================

import json
from pathlib import Path


FILE_PATH = Path(__file__).parent / "tasks.json"


def load_tasks() -> list[dict]:
    """
    Load tasks from the JSON file.
    """

    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("tasks.json must contain a list.")

        return data

    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON.")
        return []

    except OSError as error:
        print("Error reading tasks.json:", error)
        return []


def save_tasks(tasks: list[dict]) -> None:
    """
    Save tasks to the JSON file.
    """

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    except OSError as error:
        print("Error writing tasks.json:", error)