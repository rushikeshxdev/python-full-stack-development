# -------------------------------------
#              Lists
# -------------------------------------
#
# THEORY:
#
# A list is an ordered and mutable collection of elements.
#
# Ordered:
#   Elements maintain their position/index.
#
# Mutable:
#   We can add, remove, or modify elements after creation.
#
# Lists can contain different data types:
#   [10, "Python", True, 10.5]
#
# Indexing starts from 0:
#   list[0] -> first element
#   list[-1] -> last element
#
# Common list methods:
#   append() -> add item at the end
#   insert() -> add item at a specific position
#   remove() -> remove a specific item
#   pop() -> remove item using index / last item
#   len() -> number of elements
#
# ==========================================================

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])


# Adding an element
fruits.append("Grapes")
print("After append:", fruits)


# Adding at a specific position
fruits.insert(1, "Watermelon")
print("After insert:", fruits)


# Updating an element
fruits[0] = "Pineapple"
print("After update:", fruits)


# Removing an element
fruits.remove("Banana")
print("After remove:", fruits)


# Remove last element
fruits.pop()
print("After pop:", fruits)


# Length
print("Length:", len(fruits))


# Check whether an item exists
if "Mango" in fruits:
    print("Mango is available")


# Loop through list
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)