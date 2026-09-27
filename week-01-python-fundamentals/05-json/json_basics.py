# ==========================================================
# Python JSON - Basics
# ==========================================================
#
# THEORY:
#
# JSON = JavaScript Object Notation
#
# JSON is a lightweight text-based format used for storing
# and exchanging structured data.
#
# JSON is very common in:
# - REST APIs
# - Configuration files
# - Data storage
# - Communication between frontend and backend
#
# JSON supports:
# - String
# - Number
# - Boolean
# - Null
# - Object
# - Array
#
# Python equivalents:
#
# JSON object  -> Python dictionary
# JSON array   -> Python list
# JSON string  -> Python string
# JSON number  -> Python int / float
# JSON true    -> Python True
# JSON false   -> Python False
# JSON null    -> Python None
#
# ==========================================================

import json


# ----------------------------------------------------------
# 1. Python dictionary
# ----------------------------------------------------------

user = {
    "name": "Rushikesh",
    "age": 23,
    "city": "Kolhapur",
    "is_developer": True
}

print("Python dictionary:")
print(user)


# ----------------------------------------------------------
# 2. Convert Python dictionary to JSON string
#    json.dumps()
# ----------------------------------------------------------

json_string = json.dumps(user)

print("\nJSON string:")
print(json_string)

print("\nType:")
print(type(json_string))


# ----------------------------------------------------------
# 3. Convert JSON string back to Python object
#    json.loads()
# ----------------------------------------------------------

python_object = json.loads(json_string)

print("\nPython object:")
print(python_object)

print("\nType:")
print(type(python_object))


# ----------------------------------------------------------
# 4. Pretty JSON
# ----------------------------------------------------------

pretty_json = json.dumps(user, indent=4)

print("\nPretty JSON:")
print(pretty_json)


# ----------------------------------------------------------
# 5. List to JSON
# ----------------------------------------------------------

skills = [
    "Python",
    "Django",
    "Flask",
    "JavaScript"
]

skills_json = json.dumps(skills, indent=4)

print("\nSkills JSON:")
print(skills_json)


# ----------------------------------------------------------
# 6. Nested Python data
# ----------------------------------------------------------

student = {
    "name": "Rushikesh",
    "age": 23,
    "skills": [
        "Python",
        "JavaScript",
        "SQL"
    ],
    "address": {
        "city": "Kolhapur",
        "state": "Maharashtra"
    }
}

student_json = json.dumps(student, indent=4)

print("\nNested JSON:")
print(student_json)