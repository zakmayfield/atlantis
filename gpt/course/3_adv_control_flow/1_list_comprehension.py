"""
List comprehensions are concise ways to create new lists in Python, and they are generally faster than using traditional loops. 

They are written inside square brackets and consist of an expression followed by a for clause (or multiple for clauses) and optionally a if clause, which allows for filtering elements.
"""

squares = [x**2 for x in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10]

list1 = ["Hello", "World"]
list2 = ["Welcome", "to", "ChatGPT"]
concatenated_list = [x + " " + y for x in list1 for y in list2]
print(concatenated_list)
# ['Hello Welcome', 'Hello to', 'Hello ChatGPT', 'World Welcome', 'World to', 'World ChatGPT']

more_squares = [x for x in range(1, 6)]
print(more_squares)
# [1, 2, 3, 4, 5]