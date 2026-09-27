# ==========================================================
# Exception Handling Practice
# ==========================================================
#
# PURPOSE:
#
# Practice:
# - try
# - except
# - multiple exceptions
# - else
# - finally
# - raise
#
# ==========================================================


def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = divide_numbers(first_number, second_number)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as error:
    print("Error:", error)

else:
    print("Result:", result)

finally:
    print("Calculator execution completed.")