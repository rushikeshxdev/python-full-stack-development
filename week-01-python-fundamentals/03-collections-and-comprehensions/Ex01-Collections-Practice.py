# -------------------------------------
#       Collections Practice
# -------------------------------------


# 1. List of numbers

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("First number:", numbers[0])
print("Last number:", numbers[-1])


# 2. Add a number

numbers.append(60)

print("After adding 60:", numbers)


# 3. Remove a number

numbers.remove(30)

print("After removing 30:", numbers)


# 4. Find even numbers

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print("Even numbers:", even_numbers)


# 5. Student dictionary

student = {
    "name": "Rushikesh",
    "age": 23,
    "branch": "CSBS"
}

print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student branch:", student["branch"])


# 6. Add city

student["city"] = "Kolhapur"

print("Updated student:", student)


# 7. Create a set from duplicate values

values = [10, 20, 20, 30, 10, 40, 40]

unique_values = set(values)

print("Unique values:", unique_values)