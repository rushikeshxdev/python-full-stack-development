# ==========================================================
# Python Built-in Modules
# ==========================================================
#
# THEORY:
#
# Python comes with many modules in its standard library.
# We can import them instead of implementing common
# functionality ourselves.
#
# Examples:
#
# math     -> mathematical operations
# random   -> random values
# datetime -> date and time
# os       -> operating system / file operations
#
# ==========================================================


import math
import random
from datetime import datetime
import os


# math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))


# random

print("Random number:", random.randint(1, 100))


# datetime

current_time = datetime.now()

print("Current date and time:", current_time)


# os

print("Current working directory:")
print(os.getcwd())