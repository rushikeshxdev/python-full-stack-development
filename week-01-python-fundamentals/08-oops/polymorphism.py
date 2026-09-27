# ==========================================================
# OOP - Polymorphism
# ==========================================================
#
# THEORY:
#
# Polymorphism means that the same method/interface can have
# different implementations or behavior for different objects.
#
# In Python, different classes can provide a method with the
# same name, and code can call that method without needing to
# know the exact class.
#
# ==========================================================


class Dog:
    def speak(self):
        return "Dog says: Woof!"


class Cat:
    def speak(self):
        return "Cat says: Meow!"


class Cow:
    def speak(self):
        return "Cow says: Moo!"


animals = [
    Dog(),
    Cat(),
    Cow()
]


for animal in animals:
    print(animal.speak())