# ==========================================================
# OOP - Inheritance
# ==========================================================
#
# THEORY:
#
# Inheritance allows a child class to reuse and extend
# functionality from a parent class.
#
# Parent class -> common functionality
# Child class  -> specialized functionality
#
# ==========================================================


class Person:
    def __init__(self, name: str):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Developer(Person):
    def write_code(self):
        print(self.name, "is writing code.")


class Student(Person):
    def study(self):
        print(self.name, "is studying.")


developer = Developer("Rushikesh")
student = Student("Amit")

developer.introduce()
developer.write_code()

print()

student.introduce()
student.study()