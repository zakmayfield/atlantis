# inheritance 
"""
Inheritance is a mechanism in OOP that allows one class to inherit attributes and methods from another class. The class that inherits is called a subclass or derived class, and the class that is inherited from is called a superclass or base class. Inheritance allows for code reuse and promotes modularity in programming.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age}')


class Student(Person):
    pass

"""
In Python, you can define a subclass by specifying the superclass as an argument in the class definition.
"""

# Create a student object
jane = Student('Jane', 24)
austin = Student('Austin', 26)

jane.say_hello()
austin.say_hello()