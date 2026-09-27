# 2. `math_utils.py`

# ==========================================================
# Python Modules - Custom Module
# ==========================================================
#
# THEORY:
#
# A module is simply a Python file containing reusable code.
#
# Functions, classes, and variables defined in one Python
# file can be imported and used in another Python file.
#
# This helps us avoid writing the same code repeatedly.
#
# ==========================================================


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b