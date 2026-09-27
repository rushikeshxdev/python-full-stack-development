# -------------------------------------
#      Function-Based Calculator
# -------------------------------------


# Addition
def add(a: int, b: int) -> int:
    return a + b


# Subtraction
def subtract(a: int, b: int) -> int:
    return a - b


# Multiplication
def multiply(a: int, b: int) -> int:
    return a * b


# Division
def divide(a: int, b: int) -> float:
    if b == 0:
        print("Cannot divide by zero.")
    return a / b


# Modulus
def modulus(a: int, b: int) -> int:
    if b == 0:
        print("Cannot perform modulus by zero.")
    return a % b


# Take input from user
try:
    val1 = int(input("Enter the first value: "))
    val2 = int(input("Enter the second value: "))

    operation = input("Enter the operator (+, -, /, *, %): ")

    if operation == "+":
        result = add(val1, val2)

    elif operation == "-":
        result = subtract(val1, val2)

    elif operation == "*":
        result = multiply(val1, val2)

    elif operation == "/":
        result = divide(val1, val2)

    elif operation == "%":
        result = modulus(val1, val2)

    else:
        print("Invalid operator.")

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as error:
    print(error)