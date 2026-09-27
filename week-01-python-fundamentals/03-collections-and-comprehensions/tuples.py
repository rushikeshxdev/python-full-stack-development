# -------------------------------------
#              Tuples
# -------------------------------------
#
# THEORY:
#
# A tuple is an ordered and immutable collection.
#
# Ordered:
#   Elements maintain their position/index.
#
# Immutable:
#   Once a tuple is created, its elements cannot normally
#   be changed, added, or removed.
#
# Tuples use parentheses:
#   (10, 20, 30)
#
# Lists vs Tuples:
#
#   List  -> mutable
#   Tuple -> immutable
#
# Tuples are useful when data should remain unchanged.
#
# ==========================================================

# Creating a tuple
coordinates = (18.52, 73.85)

print("Coordinates:", coordinates)


# Accessing elements
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])


# Tuple with multiple values
student = ("Rushikesh", 23, "CSBS")

print("Student name:", student[0])
print("Student age:", student[1])
print("Student branch:", student[2])


# Length
print("Length:", len(student))


# Loop through tuple
print("\nStudent details:")

for value in student:
    print(value)


# Check item
if "CSBS" in student:
    print("CSBS found")


# Tuple unpacking
name, age, branch = student

print("\nUnpacked values:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)