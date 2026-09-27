# ==========================================================
# OOP - Constructor
# ==========================================================
#
# THEORY:
#
# `__init__()` is a special method called automatically when
# an object is created.
#
# It is commonly used to initialize object attributes.
#
# ==========================================================


class Student:
    def __init__(self, name: str, age: int, branch: str):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)


student1 = Student("Rushikesh", 23, "CSBS")
student2 = Student("Amit", 22, "CSE")

student1.introduce()

print()

student2.introduce()