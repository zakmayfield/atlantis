"""
Inheritance

Inheritance is a mechanism in OOP that allows a new class (called the derived class) to be based on an existing class (called the base class), inheriting its methods and attributes. This can save time and reduce redundancy in your code.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old")


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def say_hello(self):
        super().say_hello()
        print(f"I'm majoring in {self.major}")

student1 = Student('John', 22, 'Business')

student1.say_hello()