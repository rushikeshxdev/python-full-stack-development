# Python Fundamentals.

#Task1 - Ask the user info

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
City = input("Enter the city: ")

print("Hello, my name is", Name)
print("I am", Age, "years old")
print("I live in", City)

#Task2 - Age Eligibility

if Age > 18:
    print(Name,"Eligible for Voting!")
elif Age <= 18:
    print(Name, "You are under age!")
else:
    print('Enter valid age!')

#Task3 - Number Analyzer
num = int(input("Enter any number, i will analyze whether it is positive or negative & Even or Odd:"))

if num > 0:
    sign = "positive"
elif num < 0:
    sign = "negative"
else:
    sign = "zero"

if num % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print(f"{num} is {sign} and {parity}")


# Loops
for number in range(1, 10):
    if number == 5:
        continue

    print(number)