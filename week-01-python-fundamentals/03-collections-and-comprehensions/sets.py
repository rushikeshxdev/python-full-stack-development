# -------------------------------------
#               Sets
# -------------------------------------
#
# THEORY:
#
# A set is an unordered collection of unique elements.
#
# Important properties:
#
#   1. Duplicate values are automatically removed.
#   2. Sets do not use indexing like lists.
#   3. Sets are useful for membership checking and
#      mathematical set operations.
#
# Common operations:
#
#   add()        -> add an element
#   remove()     -> remove an element
#   discard()    -> remove an element without error if absent
#   |            -> union
#   &            -> intersection
#   -            -> difference
#
# ==========================================================

numbers = {10, 20, 30, 20, 10}

print("Numbers:", numbers)


# Add element
numbers.add(40)
print("After add:", numbers)


# Remove element
numbers.remove(20)
print("After remove:", numbers)


# Discard element
numbers.discard(100)
print("After discard:", numbers)


# Membership
if 30 in numbers:
    print("30 exists in the set")


# Loop
print("\nSet values:")

for number in numbers:
    print(number)


# Set operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nSet A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)