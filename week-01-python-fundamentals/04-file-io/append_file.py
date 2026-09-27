# ==========================================================
# Python File I/O - Appending Files
# ==========================================================
#
# THEORY:
#
# "a" mode is used to append data to an existing file.
#
# Existing content is preserved.
# New content is added at the end.
#
# If the file doesn't exist, Python creates it.
#
# ==========================================================


with open("output.txt", "a") as file:
    file.write("This line was added later.\n")
    file.write("This is an example of append mode.\n")


print("Data appended successfully.")