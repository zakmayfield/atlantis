# Challenge
"""
Below is code to find the smallest value from a list of values. One line has an error that will cause the code to not work as expected. Which line is it?:

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
"""

smallest = None

print(f"Before: {smallest}")

for iterator in [72, 3, 5, 23, 30]:
    if smallest is None or iterator < smallest:
        smallest = iterator
        # break was causing the for in loop to exit on first iteration
    print("Loop", iterator, smallest)

print("Smallest number:", smallest)
