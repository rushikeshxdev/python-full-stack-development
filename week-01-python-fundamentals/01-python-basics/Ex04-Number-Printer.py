# -------------------------------------
#        Number Printer
# -------------------------------------

# Print numbers from 1 to 100 using for loop

print("Numbers from 1 to 100:")

for number in range(1, 101):
    print(number)


# Print even numbers from 1 to 100

print("\nEven numbers from 1 to 100:")

for number in range(1, 101):
    if number % 2 == 0:
        print(number)


# Print numbers from 1 to 10 using while loop

print("\nNumbers from 1 to 10 using while loop:")

count = 1

while count <= 10:
    print(count)
    count += 1