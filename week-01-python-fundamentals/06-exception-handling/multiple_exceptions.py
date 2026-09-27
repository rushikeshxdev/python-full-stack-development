# ==========================================================
# Handling Multiple Exceptions
# ==========================================================
#
# THEORY:
#
# A single try block can potentially generate different types
# of exceptions.
#
# Multiple "except" blocks can be used to handle different
# exceptions separately.
#
# ==========================================================


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = first_number / second_number

    print("Result:", result)

except ValueError:
    print("Please enter valid integer values.")

except ZeroDivisionError:
    print("Second number cannot be zero.")