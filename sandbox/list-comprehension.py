my_list = [x for x in range(1, 6)]

# squaring numbers | x * x OR x ** 2 NOT x ** 3
nums = [1, 2, 3]
another_one = [x**2 for x in nums]

# Take a list of words and find only the words that start with a vowel
fruits = ["banana", "apple", "peach", "orange", "elm fig"]
starts_with_vowel = [x for x in fruits if x[0] in "aeiou"]

# Find all possible combinations of two lists
# [1, 2] [3, 4] -> [(1, 3), (1, 4), (2, 3), (2, 4)]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combinations = [[x, y] for x in list1 for y in list2]
