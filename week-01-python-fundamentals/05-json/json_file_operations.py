# ==========================================================
# Python JSON - File Operations
# ==========================================================
#
# THEORY:
#
# json.dump()
#     Python object -> JSON file
#
# json.load()
#     JSON file -> Python object
#
# This is different from:
#
# json.dumps()
#     Python object -> JSON string
#
# json.loads()
#     JSON string -> Python object
#
# Memory trick:
#
# dumps / loads -> STRING
# dump / load   -> FILE
#
# ==========================================================

import json


# ----------------------------------------------------------
# Data to store
# ----------------------------------------------------------

user = {
    "id": 1,
    "name": "Rushikesh",
    "age": 23,
    "city": "Kolhapur",
    "skills": [
        "Python",
        "JavaScript",
        "SQL"
    ]
}


# ----------------------------------------------------------
# 1. Write Python object to JSON file
# ----------------------------------------------------------

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

print("Data written to user.json")


# ----------------------------------------------------------
# 2. Read JSON file into Python object
# ----------------------------------------------------------

with open("user.json", "r") as file:
    data = json.load(file)

print("\nData read from user.json:")
print(data)


# ----------------------------------------------------------
# 3. Access JSON data using Python
# ----------------------------------------------------------

print("\nUser details:")
print("ID:", data["id"])
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])


# ----------------------------------------------------------
# 4. Loop through skills
# ----------------------------------------------------------

print("\nSkills:")

for skill in data["skills"]:
    print(skill)