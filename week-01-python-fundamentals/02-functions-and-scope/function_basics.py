#-----------------------------
# Python Functions
#-----------------------------

#Simple Function

def greet():
    print("Hello, Rushikesh!")


greet()


#Functions with Parameters

def greet_user(name):
    print("Hello, ", name)

greet_user("Rushikesh")
greet_user("Sumit")


#Functions with return values

def add(a, b):
    return a + b

result = add(10, 20)
print("Result: ", result)


#Default Parameter

def welcome(name="User"):
    print("Welcome, ", name)


welcome()
welcome("Rushikesh")


#Multiple Parameters

def introduce(name, age, city):
    print("My name is ,", name)
    print("I am", age," years old.")
    print("I live in", city)

introduce("Rushikesh", 23, "Mohol, Solapur")
