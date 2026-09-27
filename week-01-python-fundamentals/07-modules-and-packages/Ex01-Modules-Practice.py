# ==========================================================
# Modules & Packages Practice
# ==========================================================
#
# PURPOSE:
#
# Practice:
# - Custom modules
# - Importing functions
# - Built-in modules
# - Python packages
#
# ==========================================================


# Import from custom module

from math_utils import add, subtract


print("Custom module:")
print("Addition:", add(10, 20))
print("Subtraction:", subtract(20, 5))


# Import from package

from package_demo.calculator import multiply
from package_demo.greetings import greet


print("\nPackage:")
print("Multiplication:", multiply(5, 6))
print(greet("Rushikesh"))