# slicing
"""
Slicing is a way to extract a portion of a sequence, such as a string, list, or tuple. Slicing allows you to create a new sequence containing only a subset of the original elements, without modifying the original sequence

syntax:

sequence[start:end:step]

- `sequence` is the sequence you want to slice, such as a string, list, or tuple.

- `start` is the index of the starting element in the slice. It is inclusive, meaning the element at the start index is included in the slice.

- `end` is the index of the ending element in the slice. It is exclusive, meaning the element at the end index is not included in the slice.

- `step` is an optional parameter that specifies the step size or the interval between elements to include in the slice. It defaults to 1.
"""

# Slicing a string
s = 'hello, world!'
# print( s[0:5] ) # hello
# print( s[7:12] ) # world
# print( s[:5] ) # hello
# print( s[7:] ) # world
# print( s[0:12:2] ) # hlo ol

# Slicing a list
l = [1,2,3,4,5]
print( l[1:4] ) # [2, 3, 4]
print( l[:3] ) # [1, 2, 3]
print( l[::2] ) # [1, 3, 5]