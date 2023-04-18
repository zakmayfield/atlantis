# dictionaries
"""
a dictionary is a mutable, unordered collection of key-value pairs, also known as an associative array or a hash map. Dictionaries are created using curly braces ({}) and allow for efficient lookup, insertion, and deletion of values based on their keys.

dictionaries in Python are similar to JavaScript objects in terms of their functionality. Both dictionaries in Python and objects in JavaScript allow for the creation of key-value pairs, where keys are unique identifiers and values are associated with those keys.
"""

# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
}

# Accessing dictionary elements
name = my_dict['name']
age = my_dict.get('age')

# Adding and modifying dictionary elements
my_dict['email'] = 'john@email.com'
my_dict.pop('city')

# Checking dictionary keys and values
keys = my_dict.keys()
values = my_dict.values()
is_key_present = 'city' in my_dict # False