# ==========================================================
# Using a Custom Module
# ==========================================================
#
# THEORY:
#
# We can import reusable functions from another Python file.
#
# Example:
#
#     import math_utils
#
# Then:
#
#     math_utils.add(10, 20)
#
# ==========================================================


import math_utils


result1 = math_utils.add(10, 20)
result2 = math_utils.subtract(20, 5)
result3 = math_utils.multiply(5, 4)
result4 = math_utils.divide(20, 5)

print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)