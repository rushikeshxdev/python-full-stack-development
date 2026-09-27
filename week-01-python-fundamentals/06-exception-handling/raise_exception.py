# ==========================================================
# Raising Exceptions
# ==========================================================
#
# THEORY:
#
# Sometimes we want to deliberately stop an operation when
# a business rule is violated.
#
# Python provides the "raise" keyword for this.
#
# Example:
#
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#
# ==========================================================


def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        raise ValueError("User must be at least 18 years old.")


try:
    user_age = int(input("Enter your age: "))

    validate_age(user_age)

    print("Age is valid.")

except ValueError as error:
    print("Error:", error)