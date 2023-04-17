# String methods
"""
String methods in Python are built-in functions that allow you to perform various operations on strings, which are sequences of characters.

some methods include:

- len()
- lower()
- upper()
- strip()
- split()
- replace()
- find()
- startswith()
- endswith()
- join()
"""

space = "  Hello, World!         "
print(space.strip())

string_list = space.split()
print(string_list)

list = ["Hello", "World!"]
joined = ", ".join(list)
print(joined)

universal = space.replace("World", "Universe").strip()
print(universal)
