"""
Higher Order Functions

In Python, functions are considered first-class objects, which means they can be passed around just like any other value. This allows us to create higher order functions, which are functions that take other functions as args and/or return functions as values
"""

# Example


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# HOF
def operate(a, b, func):
    return func(a, b)


res = operate(10, 5, subtract)
print(res)
