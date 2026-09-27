# -------------------------------------
#            Dictionaries
# -------------------------------------
#
# THEORY:
#
# A dictionary stores data in KEY : VALUE pairs.
#
# Example:
#
#   {
#       "name": "Rushikesh",
#       "age": 23
#   }
#
# "name" -> key
# "Rushikesh" -> value
#
# Important properties:
#
#   - Data is accessed using keys.
#   - Keys should be unique.
#   - Dictionaries are mutable.
#
# Common operations:
#
#   dict[key]         -> access value
#   get()             -> safely access value
#   dict[key] = value -> add/update
#   pop()             -> remove
#   keys()            -> get keys
#   values()          -> get values
#   items()           -> get key-value pairs
#
# Dictionaries are commonly used for structured data and
# are very similar to JSON objects.
#
# ==========================================================

# Creating a dictionary
student = {
    "name": "Rushikesh",
    "age": 23,
    "branch": "CSBS",
    "college": "KIT"
}

print("Student:", student)


# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])


# Using get()
print("Branch:", student.get("branch"))


# Adding a new key
student["city"] = "Kolhapur"

print("After adding city:", student)


# Updating a value
student["age"] = 24

print("After updating age:", student)


# Removing a key
student.pop("college")

print("After removing college:", student)


# Check key
if "name" in student:
    print("Name key exists")


# Get all keys
print("\nKeys:")
for key in student.keys():
    print(key)


# Get all values
print("\nValues:")
for value in student.values():
    print(value)


# Get key-value pairs
print("\nKey-Value pairs:")

for key, value in student.items():
    print(key, ":", value)