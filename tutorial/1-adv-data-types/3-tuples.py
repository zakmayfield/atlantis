#tuples
"""
A tuple is an immutable collection of ordered, comma-separated values enclosed in round parentheses (). Tuples are similar to lists in Python, but unlike lists, tuples cannot be modified once they are created, making them immutable.

Tuples are used to store and represent a fixed sequence of values, and they can contain values of different data types, such as numbers, strings, or even other tuples. Tuples are commonly used to represent a collection of related values that should remain unchanged, such as coordinates, dates, or color codes.
"""

# Creating a tuple
my_tuple = (1,2,2,2,3,4,5)

# Accessing elements in the tuple
first_el = my_tuple[0]
last_el = my_tuple[-1]

# Tuple packing and unpacking
a = 1
b = 2
a_b = a, b
print(a_b) # (1, 2)
c, d = a_b
print(c, d) # 1 2

# Tuple operations
tuple_len = len(my_tuple)
print(tuple_len) # 7
tuple_count = my_tuple.count(2)
print(tuple_count) # 3

is_element_present = 3 in my_tuple
print(is_element_present) # True

# Immutable
try:
  my_tuple[0] = 10
except:
  print('ya done goofed. this is immutable')
