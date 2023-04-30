"""
I/O Operations

I/O (Input/Output) operations are the ways in which a program communicates with the outside world. Input operations are used to get data into a program, while output operations are used to display or save data produced by the program.

examples of input operations include reading data from a keyboard, a file, or a database. Some examples of output operations include displaying data on a screen, writing data to a file, or sending data over a network.
"""

"""
Input operations

In Python, you can take user input using the built-in input() function, which prompts the user to enter a value, and returns the entered value as a string
"""

# Example

name = input('Enter your name: ')
print(f'Hello, {name}')

"""
You can convert the input data type to another data type using type casting. 
"""

age = int(input('Enter your age: '))
print(age)

"""
Output operation: print()
"""

my_name = 'zak'
my_age = 28
print("My name is {}, and i'm {} years old".format(my_name, my_age))