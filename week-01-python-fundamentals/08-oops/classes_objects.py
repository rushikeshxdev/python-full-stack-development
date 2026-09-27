# ==========================================================
# OOP - Classes and Objects
# ==========================================================
#
# THEORY:
#
# A CLASS is a blueprint for creating objects.
#
# An OBJECT is an instance of a class.
#
# A class can contain:
# - Attributes -> data/state
# - Methods    -> behavior/actions
#
# Example:
#
# Class  -> Student
# Object -> Rushikesh
#
# ==========================================================


class Student:
    def introduce(self):
        print("I am a student.")


# Creating objects

student1 = Student()
student2 = Student()


# Calling methods

student1.introduce()
student2.introduce()

class Student:
    name = "Unknown"
    branch = "Unknown"

    def introduce(self):
        print("Name:", self.name)
        print("Branch:", self.branch)


student1 = Student()
student1.name = "Rushikesh"
student1.branch = "CSBS"

student1.introduce()