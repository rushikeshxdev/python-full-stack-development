# -------------------------------------
#       *args and **kwargs
# -------------------------------------


# 1. *args
# Accepts multiple positional arguments
def show_numbers(*args):
    print("args:", args)
    print("Type of args:", type(args))


show_numbers(10, 20, 30)


# 2. Using *args in a calculation
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print("Total:", add_numbers(10, 20, 30, 40))


# 3. **kwargs
# Accepts multiple keyword arguments
def show_user(**kwargs):
    print("kwargs:", kwargs)
    print("Type of kwargs:", type(kwargs))


show_user(
    name="Rushikesh",
    age=23,
    city="Kolhapur"
)


# 4. Reading values from **kwargs
def print_user_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print_user_details(
    name="Rushikesh",
    age=23,
    role="Developer"
)


# 5. Using both *args and **kwargs
def example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


example(
    10,
    20,
    30,
    name="Rushikesh",
    city="Kolhapur"
)


# 6. * unpacking
numbers = (10, 20, 30)

def add(a, b, c):
    return a + b + c


print("Using * unpacking:", add(*numbers))


# 7. ** unpacking
user = {
    "name": "Rushikesh",
    "age": 23
}


def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce(**user)