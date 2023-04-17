# encapsulation
"""
Encapsulation in Python is a mechanism that allows the hiding of implementation details of an object's attributes or methods from the external world, and restricting direct access to them. It is one of the fundamental principles of object-oriented programming (OOP) and provides the ability to control the visibility and accessibility of data members and methods of a class.

Encapsulation can be achieved by using access modifiers, which are special keywords that define the visibility and accessibility of class members. There are three common access modifiers used in Python:

- `Public`: Members declared as public are accessible from anywhere in the program. In Python, all members of a class are public by default.

- `Private`: Members declared as private are only accessible within the class itself. In Python, private members are denoted by a double underscore prefix before the member name, such as __private_member.

- `Protected`: Members declared as protected are accessible within the class itself and its subclasses. In Python, protected members are denoted by a single underscore prefix before the member name, such as _protected_member.
"""

class Car:
    def __init__(self, make, model, year) -> None:
        self.__make = make # private
        self._model = model # protected
        self.year = year # public

    def display_info(self):
        print(f'Make: {self.__make}')
        print(f'Model: {self._model}')
        print(f'Year: {self.year}')

carl = Car('Toyota', 'Camry', 2022)

print(carl.year)
print(carl._model)

"""
 `__make` is a private member, `_model` is a protected member, and `year` is a public member. 
 
 The display_info() method can access all members, but external code can only access the public member year directly. Accessing private and protected members directly from outside the class is generally discouraged, and it is recommended to use methods provided by the class to access or modify those members, if needed.
"""