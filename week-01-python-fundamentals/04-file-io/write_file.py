# ==========================================================
# Python File I/O - Writing Files
# ==========================================================
#
# THEORY:
#
# "w" mode is used for writing data to a file.
#
# Important:
#
# If the file already exists, "w" will overwrite its content.
#
# If the file does not exist, Python will create it.
#
# Example:
#
#     with open("file.txt", "w") as file:
#         file.write("Hello")
#
# ==========================================================


# Write content to a file

with open("output.txt", "w") as file:
    file.write("Hello, Rushikesh!\n")
    file.write("I am learning Python File I/O.\n")
    file.write("This file was created using Python.\n")


print("Data written successfully.")