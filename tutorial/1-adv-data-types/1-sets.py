# Sets
"""
collection of unique elements, where each element must be immutable (i.e., unchangeable), and the elements are unordered. Sets are defined using curly braces {} and elements are separated by commas.

Some key points about sets in Python:

- Unique elements: Sets only allow unique elements. If you try to add a duplicate element to a set, it will be ignored.

- Unordered: The elements in a set are unordered, meaning that the order in which elements are added to the set is not preserved.

- Mutable: Sets are mutable, meaning that you can add and remove elements from a set after it is created.

- Immutable elements: Elements in a set must be immutable, meaning that they cannot be changed after they are added to the set. Examples of immutable elements include numbers, strings, and tuples.

- No duplicate elements: Sets automatically eliminate duplicate elements. If you try to add a duplicate element to a set, it will be ignored.

- Set operations: Sets support various set operations such as union, intersection, difference, and symmetric difference, which can be useful for performing set-based operations on collections of data.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(60)
my_set.update([700, 800, 900])

# Removing items from a set
my_set.remove(3)
my_set.discard(60)

# Retains unique elements with no dupes
my_set.add(1)

# union()
"""
operation that combines two or more sets into a single set, containing all the unique elements from the original sets. The union operation is denoted by the pipe "|" symbol or by using the union() method. 
"""
set1 = {1,2}
set2 = {2,3}
union_set = set1.union(set2)

# intersection()
"""
operation that allows you to find the common elements between two or more sets. It can be performed using the intersection() method or the
"""

set3 = {1,2}
set4 = {2,3}
intersection_set = set1.intersection(set2)

# difference()
"""
used to find the elements that are present in one set but not in another. It is denoted by the "-" (minus) operator or can be invoked using the difference() method.
"""

set4 = {1,2}
set5 = {2,3}
difference_set = set1.difference(set2) # {1}
difference_set = set2 - set1 # {3}

# issubset()
"""
used to determine if a set is a subset of another set. It returns True if all the elements of the calling set are present in the set specified as an argument, and False otherwise.
"""

set6 = {1, 2, 3}
set7 = {1, 2, 3, 4, 5, 6}
subset_set = set6.issubset(set7)

# print(my_set) # {1, 2, 4, 5, 900, 800, 700}
# print(union_set) # {1, 2, 3}
# print(intersection_set) # {2}
# print(difference_set) # {2}
# print(subset_set) # True

# iterating
loopable = {1,2}

if 2 in loopable:
    print('2 is the magic number')

for el in loopable:
    print(el)