# is
"""
Comparison operator that checks if two objects refer to the same memory location, i.e., they have the same identity. It is used to compare the memory addresses of two objects to determine if they are the same object or not, rather than comparing their values.
"""

a = 0
b = 1

result = a is b

print(result)