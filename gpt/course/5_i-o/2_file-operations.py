"""
File Operations:

In Python, you can read and write data to files using the built-in functions open(), read(), write(), and close(). The open() function is used to open a file, 

the read() function is used to read data from a file, 

the write() function is used to write data to a file, 

the close() function is used to close a file.
"""

# file = open('gpt/course/5_i-o/example.txt', 'r')
# content = file.read()
# print(content)
# file.close()

"""
In this example, the open() function is used to open the file "example.txt" in read mode ("r"). The read() function is used to read the content of the file into the content variable. The print() function is used to display the content in the console. Finally, the close() function is used to close the file.
"""

"""
Writing Data
"""

# Appending with "a"

# file = open("gpt/course/5_i-o/example.txt", "a")
# file.write("\nHello, world.")
# file.close()

# file = open("gpt/course/5_i-o/example.txt", "r")
# content = file.read()
# print(content)
# file.close()


"""
Creating a new file and writing to it using "x"

Note: if you try to open a file in "x" mode and the file already exists, a FileExistsError will be raised.
"""

new_file = open('gpt/course/5_i-o/new_file.txt', 'x')
new_file.write('This is a newly created file.')
new_file.close()

new_file = open("gpt/course/5_i-o/new_file.txt", "r")
content = new_file.read()
print(content)
new_file.close()