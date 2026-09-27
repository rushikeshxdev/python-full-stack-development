# ==========================================================
# Python Exception Handling - Basics
# ==========================================================
#
# THEORY:
#
# An exception is an error that occurs while a program is running.
#
# Without exception handling, an unexpected error can terminate
# the program.
#
# Python uses:
#
#     try
#     except
#
# The code that may fail goes inside "try".
# The code that handles the error goes inside "except".
#
# ==========================================================


# Example 1: ValueError

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid number.")


# Example 2: ZeroDivisionError

try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Example 3: IndexError

try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Index is out of range.")


# Example 4: KeyError

try:
    user = {
        "name": "Rushikesh"
    }

    print(user["age"])

except KeyError:
    print("Requested key does not exist.")