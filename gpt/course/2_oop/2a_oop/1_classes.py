"""
Classes & Objects
In Python, everything is an object. An object is a self-contained unit of data and associated behaviors, represented by a class. A class is like a blueprint or template for creating objects.

To define a class, use the class keyword, followed by the class name (by convention, class names start with a capital letter), and a colon. The class body contains methods (functions defined inside the class) and attributes (variables defined inside the class).
"""

# Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old")

"""
To create an object from a class, call the class as if it were a function, passing any necessary arguments to the constructor method (__init__), which is called automatically when the object is created.
"""

me = Person('Zak', 28)
me.say_hello()
