# ==========================================================
# JSON Practice
# ==========================================================
#
# PURPOSE:
#
# This exercise combines:
# - Python dictionaries
# - Python lists
# - JSON serialization
# - JSON deserialization
# - JSON file writing
# - JSON file reading
#
# This is preparation for the JSON-based Task Manager.
#
# ==========================================================

import json


# ----------------------------------------------------------
# 1. Create task data using Python
# ----------------------------------------------------------

tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "status": "completed"
    },
    {
        "id": 2,
        "title": "Learn JSON",
        "status": "pending"
    },
    {
        "id": 3,
        "title": "Build CRUD",
        "status": "pending"
    }
]


# ----------------------------------------------------------
# 2. Convert Python list to JSON string
# ----------------------------------------------------------

tasks_json = json.dumps(tasks, indent=4)

print("JSON data:")
print(tasks_json)


# ----------------------------------------------------------
# 3. Write tasks to JSON file
# ----------------------------------------------------------

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

print("\nTasks saved successfully.")


# ----------------------------------------------------------
# 4. Read tasks from JSON file
# ----------------------------------------------------------

with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)

print("\nTasks loaded from file:")
print(loaded_tasks)


# ----------------------------------------------------------
# 5. Display individual tasks
# ----------------------------------------------------------

print("\nTask List:")

for task in loaded_tasks:
    print(
        task["id"],
        "-",
        task["title"],
        "-",
        task["status"]
    )


# ----------------------------------------------------------
# 6. Add a new task
# ----------------------------------------------------------

new_task = {
    "id": 4,
    "title": "Learn Flask",
    "status": "pending"
}

loaded_tasks.append(new_task)


# ----------------------------------------------------------
# 7. Save updated tasks
# ----------------------------------------------------------

with open("tasks.json", "w") as file:
    json.dump(loaded_tasks, file, indent=4)

print("\nNew task added and JSON updated.")