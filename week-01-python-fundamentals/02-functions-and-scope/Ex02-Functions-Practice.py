# -------------------------------------
#         Functions Practice
# -------------------------------------


# 1. Check whether a number is even
def is_even(number: int) -> bool:
    return number % 2 == 0


print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


# 2. Find maximum of two numbers
def find_max(a: int, b: int) -> int:
    if a > b:
        return a
    return b


print("Maximum:", find_max(10, 25))


# 3. Calculate square of a number
def calculate_square(number: int) -> int:
    return number * number


print("Square:", calculate_square(6))


# 4. Calculate area of rectangle
def calculate_area(length: float, width: float) -> float:
    return length * width


print("Area:", calculate_area(10.5, 5.0))


# 5. Calculate average of three numbers
def calculate_average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


print("Average:", calculate_average(80, 70, 90))