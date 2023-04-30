"""
Exceptions

In Python, exception handling is a mechanism that allows you to gracefully handle errors and exceptions that might occur during the execution of your program. By using exception handling, you can prevent your program from crashing and provide a meaningful message to the user about the error that occurred.

The basic syntax for handling exceptions in Python is as follows:

try:
    # code that might raise an exception
except ExceptionType:
    # code to handle the exception
finally:
    # code that will always be executed, regardless of whether an exception was raised or not

The try block is where you put the code that might raise an exception. If an exception is raised, the program jumps to the except block, which contains the code to handle the exception. The finally block is optional and contains code that will always be executed, regardless of whether an exception was raised or not.
"""

# Example


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print(f"The result of {x}/{y} is {result}")
    finally:
        print("Always runs")


# print(divide(10, 5))
# print(divide(10, 0))


"""
Multiple exceptions

If you want to handle multiple exceptions, you can specify multiple except blocks, each one handling a different type of exception. You can also catch all exceptions by using a generic except block that catches all exceptions.

try:
    # code that might raise exceptions
except ValueError:
    # code to handle ValueError exception
except TypeError:
    # code to handle TypeError exception
except:
    # code to handle all other exceptions
"""

# Example

# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
# except ValueError:
#     print("Error: Please enter only integers")
# except ZeroDivisionError:
#     print("Error: cannot divide by zero")
# except Exception as e:
#     print(f"An error occured: {e}")
# else:
#     result = x / y
#     print(f"The result of is {x}/{y} {result}")


"""
Custom Exception Handling

you can define your own custom exceptions by creating a new class that inherits from the Exception class or one of its subclasses.

The custom exception inherits from the built-in Exception class. We don't define any new methods or attributes for the class, so it just inherits all the behavior of the Exception class.
"""

# Example

class NegativeNumberException(Exception):
    pass

def square(x):
  if x < 0:
      raise NegativeNumberException('Input number must be non-negative')
  return x*2

# print(square(-5))


# Example

class NonStringException(Exception):
    pass

def greeting(name):
    if type(name) != str:
        raise NonStringException('Input must be a string')
    
    return f"Hello there, {name}"

print(greeting('Zak'))