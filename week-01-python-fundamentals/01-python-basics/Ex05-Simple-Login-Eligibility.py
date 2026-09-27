# -------------------------------------
#     Simple Login / Eligibility
# -------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")


# Age eligibility

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")