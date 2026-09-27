# -------------------------------------
#          Comprehensions
# -------------------------------------
#
# THEORY:
#
# A comprehension is a concise way to create a collection
# from an existing iterable.
#
# Instead of writing multiple lines using a loop, we can
# sometimes create the same collection in a single readable
# expression.
#
#
# LIST COMPREHENSION:
#
#   [expression for item in iterable]
#
# Example:
#
#   squares = [x * x for x in numbers]
#
#
# LIST COMPREHENSION WITH CONDITION:
#
#   [expression for item in iterable if condition]
#
# Example:
#
#   even = [x for x in numbers if x % 2 == 0]
#
#
# DICTIONARY COMPREHENSION:
#
#   {key: value for item in iterable}
#
# Comprehensions make code shorter, but they should remain
# readable. A normal loop is sometimes better for complex logic.
#
# ==========================================================

# 1. Basic list comprehension

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print("Squares:", squares)


# 2. List comprehension with range()

even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print("Even numbers:", even_numbers)


# 3. Odd numbers

odd_numbers = [number for number in range(1, 11) if number % 2 != 0]

print("Odd numbers:", odd_numbers)


# 4. Filter numbers greater than 5

large_numbers = [number for number in range(1, 11) if number > 5]

print("Numbers greater than 5:", large_numbers)


# 5. Convert names to uppercase

names = ["rushikesh", "amit", "rahul"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)


# 6. List comprehension with condition

marks = [35, 45, 67, 80, 25, 90]

passed_marks = [mark for mark in marks if mark >= 40]

print("Passed marks:", passed_marks)


# 7. Dictionary comprehension

numbers = range(1, 6)

square_dict = {
    number: number * number
    for number in numbers
}

print("Square dictionary:", square_dict)


# 8. Dictionary comprehension with condition

even_square_dict = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}

print("Even square dictionary:", even_square_dict)