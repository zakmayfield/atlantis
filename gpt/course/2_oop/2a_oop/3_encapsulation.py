"""
Encapsulation

Encapsulation is the practice of hiding the internal details of an object from the outside world, by defining private methods and attributes that cannot be accessed or modified from outside the class.

The three access modifiers in Python are:

Public: Denoted by no preceding underscores, public attributes and methods can be accessed from anywhere, both within and outside the class.

Protected: Denoted by a single underscore before the attribute or method name, protected attributes and methods can only be accessed from within the class and its subclasses.

Private: Denoted by two underscores before the attribute or method name, private attributes and methods can only be accessed from within the class.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")


my_account = BankAccount("12345", 1000.0)

print(my_account.get_balance())
my_account.deposit(522)
print(my_account.get_balance())
my_account.withdraw(965)
print(my_account.get_balance())

# print(my_account.balance) # AttributeError