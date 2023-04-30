"""
Decorators

Decorators are a way to modify or enhance the behavior of a function without changing its source code. They allow you to wrap a function inside another function that can add some additional functionality, such as logging, timing, or input validation.

Use Decorator Syntax

def timer_decorator(func):
    def wrapper():
        ...
    return wrapper

@timer_decorator
def sleepy():
    time.sleep(2)

Where decorator_function is the function that will modify the behavior of function_name.
"""

# Examples

# Timing a Function

import time

# help(time)


def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time taken: {end_time - start_time}")

    return wrapper


@timer_decorator
def sleepy():
    time.sleep(2)


# sleepy()


# Logging function calls
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger_decorator
def add_numbers(a, b):
    return a + b


# add_numbers(2, 3)


# Validate the input arguments of a function, raise exception if the args do not meet a certain condition.
def validate_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int) or args[0] < 0 or not isinstance(args[1], int):
            raise ValueError("Input must consist of numbers")
        return func(*args, **kwargs)

    return wrapper


@validate_decorator
def add_nums(a, b):
    return a + b


# add_nums(2, "hi")


# Validate ONE argument in a function
def validate_str_input(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Input must be a string")

        return func(*args, **kwargs)

    return wrapper


@validate_str_input
def greeting(name):
    return f"Hello there, {name}."


print(greeting("Zak"))
