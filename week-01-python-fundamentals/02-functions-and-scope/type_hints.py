# -------------------------------------
#           Type Hints
# -------------------------------------


# 1. Type hints for parameters and return value

def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)
print("Addition:", result)


# 2. String type hint

def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Rushikesh")
print(message)


# 3. Float type hint

def calculate_average(total: float, count: int) -> float:
    return total / count


average = calculate_average(450.0, 5)
print("Average:", average)


# 4. Boolean type hint

def is_adult(age: int) -> bool:
    return age >= 18


print("Is adult:", is_adult(23))


# 5. List type hint

def get_names() -> list[str]:
    return ["Rushikesh", "Amit", "Rahul"]


names = get_names()
print("Names:", names)


# 6. Dictionary type hint

def get_user() -> dict[str, str]:
    return {
        "name": "Rushikesh",
        "city": "Kolhapur"
    }


user = get_user()
print("User:", user)


# 7. Type hints with None

def print_message(message: str) -> None:
    print(message)


print_message("Learning Python Type Hints")