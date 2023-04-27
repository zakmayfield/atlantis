"""
List comprehensions are concise ways to create new lists in Python, and they are generally faster than using traditional loops. 

They are written inside square brackets and consist of an expression followed by a for clause (or multiple for clauses) and optionally a if clause, which allows for filtering elements.

The basic syntax of list comprehensions is as follows:

new_list = [expression for item in iterable if condition]

`new_list`: The new list that will be created.
`expression`: The expression that will be evaluated and added to the new list.
`item`: The variable that takes on the value of each item in the iterable object.
`iterable`: The iterable object to iterate over.
`if condition`: An optional condition to filter items from the iterable.
"""

# Examples

# Square numbers {{ x**2 or x*x }}
squares = [x**2 for x in range(1, 6)]



# Filter numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]  # even
odd_numbers = [num for num in numbers if num % 2 != 0]  # odd
# Combine even_numbers and odd_numbers to a single ascending list
numbers_asc = sorted(even_numbers + odd_numbers)



# Generate a list of words that start with a vowel from a given list of words.

# This was my attempt before asking ChatGPT for a better version
words = ["banana", "apple", "elephant", "kangaroo"]
vowels = ["a", "e", "i", "o", "u"]
vowel_list = [x for x in words if list(x)[0] in vowels]

# ChatGPT suggested this is a more performant way to write this logic
words_2 = ["hello", "world", "my", "name", "is", "Anna"]
vowel_list_2 = [word for word in words if word[0] in "aeiou"]

# Repitition makes perfection
fruits = ["banana", "apple", "peach", "orange"]
starts_with_vowel = [x for x in fruits if x[0] in "aeiou"]



# Generate a list of all possible combinations of two lists.
# should translate to [1, 2] and [3, 4] -> [(1,3), (1,4), (2,3), (2,4)]
list1 = [1, 2]
list2 = [3, 4]

combinations = [(x ,y) for x in list1 for y in list2]
print(combinations)