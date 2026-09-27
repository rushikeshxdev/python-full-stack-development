# ==========================================================
# Python File I/O - Reading Files
# ==========================================================
#
# THEORY:
#
# File I/O means reading data from or writing data to files.
#
# To work with a file, Python commonly uses:
#
#     open()
#
# Common read methods:
#
#     read()       -> reads the complete file
#     readline()   -> reads one line
#     readlines()  -> reads all lines into a list
#
# File mode:
#
#     "r" -> read mode
#
# Recommended approach:
#
#     with open(...) as file:
#         ...
#
# The "with" statement automatically closes the file after
# the operation is complete.
#
# ==========================================================


# Reading the complete file

with open("sample.txt", "r") as file:
    content = file.read()

print("Complete file:")
print(content)


# Reading one line

with open("sample.txt", "r") as file:
    first_line = file.readline()

print("\nFirst line:")
print(first_line)


# Reading all lines

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nAll lines:")
print(lines)


# Reading line by line

print("\nReading line by line:")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())