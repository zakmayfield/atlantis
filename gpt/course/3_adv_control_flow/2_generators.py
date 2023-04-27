"""
Generators are a type of iterable, like lists or tuples. But unlike lists, generators do not store all the values in memory at once. Instead, they generate the values on-the-fly as you iterate over them. This makes generators much more memory-efficient than lists, especially when dealing with large datasets.

Syntax

The basic syntax of a generator function is similar to that of a normal function, but instead of using the return keyword, it uses yield to return a value and temporarily suspend the function's execution state.

def generator_function():
    yield value

"""

# Generators


# Fibonacci Sequence - The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers. It starts with 0 and 1, and then each subsequent number is the sum of the previous two numbers. So it goes like this: 0, 1, 1, 2, 3, 5, 8, 13... `8 + 13` = 21, `13 + 21` = 34, ect


# Generate the Fibonacci sequence up to a certain number
def fibonacci(n):
    # declare two variables starting at 0 and 1
    a, b = 0, 1
    # loop while a is less than certain number yield a
    while a < n:
        yield a
        # set 'a' with next iterated number, set 'b' to both numbers added - start the loop again until number is met
        a, b = b, a + b


fib = fibonacci(100)
# print(fib)


# Read a large file line by line using a generator function
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


# for line in read_large_file("gpt/course/3_adv_control_flow/example_file/test.txt"):
#     print(line)

"""
Context 

In Python, a context is a block of code that has a defined beginning and end and is associated with some resource that needs to be managed. When the context begins, the resource is acquired and made available to the code inside the block. When the context ends, the resource is automatically released and any necessary cleanup is performed.

In our example:

def read_large_file (file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

Context starts when the 'with' statement is executed, and ends when the following indented block is exited. This means that any code that depends on the file being open and available for use needs to be placed within the indented block following the context creation.

If you were to attempt to continue this function but exit the indentation, the function would no longer have access to the file because the context ended.

def read_large_file (file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
    # any code block placed here
      #  will not have access to the file context
"""

# Practice questions

# 1.) Generate a sequence of prime numbers up to a certain number using a generator function (Sieve of Eratosthenes)

def prime_numbers(n):
    is_prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if is_prime[num]:
            yield num
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = False

primes = prime_numbers(121)

# for x in primes:
#     print(x)

# Written step progression for the Sieve of Eratosthenes

# 2*2 = 4 step 2 : 4, 6, 8, 10, 12, 14... == not primes
# 3 was not marked as not prime so start at 3
# 3*3 = 9 step 3 : 9, 12, 15, 18, 21, 24, 27... == not primes
# 4 was marked as prime in the 2 iteration so move to 5
# 5*5 = 25 step 5 : 25, 30, 35, 40, 45... == not primes
# 6 was marked as prime in the 2 iteration so move to 7
# 7*7 = 49 step 7 : 49, 56, 63, 70... == not primes
# 8 is not prime, move to 9, 9 is not prime from the 3 iteration move to 10, 10 is not prime, move to 11
# 11 * 11 = 121 step 11 : 121, 132, 143, 154... and so on until the final number is met



# 2.) Create a generator function that returns all possible combinations of a given list.

def list_combos (list):
    for x in range(1, len(list) + 1):
        for j in range(len(list) - x + 1):
          yield (list[j:j+x])

# for combo in list_combos([1, 2, 3, 4]):
#     print(combo)



# 3.) Use a generator expression to calculate the sum of squares of even numbers up to 100.
my_sum = sum(x**2 for x in range(2, 101, 2))
# print(my_sum)