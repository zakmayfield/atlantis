"""
Object-oriented programming (OOP) is a programming paradigm that uses objects, which are instances of classes, to represent and manipulate data. Python is an object-oriented programming language that supports OOP principles, including classes, objects, inheritance, encapsulation, and polymorphism.

In Python, a class is a blueprint for creating objects, which are instances of that class. A class defines the structure and behavior of objects. To create a class, you use the class keyword followed by the class name, and a pair of parentheses. 
"""

# Creating a Person class
"""
Declare a class with the `class` keyword
"""
class Test:
    pass # empty class gets passed this 'pass' statement



# Creating new objects from the class
"""
To create an object of a class, you need to instantiate the class by calling the class name followed by parentheses, like a function. This creates a new object, also known as an instance, of the class.
"""

test1 = Test()
test2 = Test()

# Attributes and methods
"""
Classes can have attributes, which are variables that store data, and methods, which are functions that define the behavior of objects. Attributes and methods are accessed using the dot (.) operator on objects.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age}')

jon_snow = Person('Jon', 24)

# jon_snow.say_hello() 

"""
__init__ method initializes the attributes name and age of the Person object.

similar to a constructor in javascript, self = this
"""