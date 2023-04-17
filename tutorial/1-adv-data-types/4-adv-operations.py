# Advanced Operations
"""
Sorting, slicing, and comprehensions are advanced operations that can be applied to sets, dictionaries, and tuples.

Will go through a few examples but this requires further exploration.
"""

# sort
"""
built-in method in Python that sorts the elements of a list in ascending order. It modifies the original list and does not return a new list
"""
my_list = [4,7,2,1,3]
my_list.sort()
print(my_list) # [1, 2, 3, 4, 7]

# sorted
"""
built-in function in Python that returns a new sorted list without modifying the original list. It can sort a list in ascending or descending order, and can also take a key argument for custom sorting based on a specific property of the elements
"""
anotha_one = [2,6,1,5]
anotha_one_desc = sorted(anotha_one, reverse=True)
print(anotha_one_desc) # [6, 5, 2, 1]

words =['banana', 'foo', 'hi']
sorted_words = sorted(words, key=len)
print(sorted_words) #['hi', 'foo', 'banana']

# custom sorting
more_words = ['hello', 'hi', 'goodbye', 'bye']

def sort_by_len(el):
    return len(el)

more_words.sort(key=sort_by_len)

print(more_words) #['hi', 'bye', 'hello', 'goodbye']