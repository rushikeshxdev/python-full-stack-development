# ==========================================================
# Python File I/O - File Modes
# ==========================================================
#
# THEORY:
#
# Python provides different modes when opening a file.
#
# "r" -> Read
# "w" -> Write / overwrite
# "a" -> Append
# "x" -> Create new file
#
# Additional modes:
#
# "b" -> Binary mode
# "+" -> Read and write
#
# Examples:
#
# "rb" -> Read binary
# "wb" -> Write binary
# "r+" -> Read and write
#
# ==========================================================


# Read mode
with open("sample.txt", "r") as file:
    print(file.read())


# Write mode
with open("write-demo.txt", "w") as file:
    file.write("This is write mode.")


# Append mode
with open("write-demo.txt", "a") as file:
    file.write("\nThis is append mode.")


print("File mode examples completed.")