# ==========================================================
# File Operations Practice
# ==========================================================
#
# PURPOSE:
#
# Practice file creation, writing, reading, appending and
# handling a file that may not exist.
#
# ==========================================================

import os


file_name = "student.txt"


# 1. Check whether file exists

if os.path.exists(file_name):
    print("File already exists.")
else:
    print("File does not exist. Creating it...")


# 2. Write student information

with open(file_name, "w") as file:
    file.write("Name: Rushikesh\n")
    file.write("Age: 23\n")
    file.write("Branch: CSBS\n")

print("Student information written.")


# 3. Append new information

with open(file_name, "a") as file:
    file.write("City: Kolhapur\n")

print("City added.")


# 4. Read the file

with open(file_name, "r") as file:
    content = file.read()

print("\nStudent Information:")
print(content)