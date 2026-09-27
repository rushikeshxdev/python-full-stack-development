# Week1 : Task1 - Python Basics

# 1. Variables:

name = "Rushikesh"
age = 23
height = 6.1
is_developer = True

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Developer: ", is_developer)


# 2. DataTypes:

integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True

print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))


# 3. Operators:

a = 20
b = 5

print("Addition: ", a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Modulus: ", a%b)


# 4. Input

user_name = input("Enter your name: ")
print("Hello,", user_name)


# 5. Conditions

marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 6. Loops

for number in range(1, 6):
    print("Number: ", number)

count = 1

while count <= 5:
    print("Count:", count)
    count += 1