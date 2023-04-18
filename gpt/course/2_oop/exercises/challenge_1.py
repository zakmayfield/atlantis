"""
Classes

You are tasked with modeling a simple library system. The library has books, and each book has a title, author, genre, and availability status (i.e., whether it is currently borrowed or not).

Requirements:

1.) Create a class called Book that represents a book in the library. The Book class should have the following attributes:

* `title`: a string representing the title of the book
* `author`: a string representing the author of the book
* `genre`: a string representing the genre of the book
* `available`: a boolean value representing the availability status of the book (True if available, False if borrowed)

2.) Define a method display_info() within the Book class that displays the information of the book, including its title, author, genre, and availability status.

3.) Instantiate three Book objects with different attributes to represent three books in the library.

Steps:

1.) Create a new Python file and define the Book class with the attributes and method as described in the requirements.

2.) Instantiate three Book objects with different attributes to represent three books in the library.

3.) Call the display_info() method on each Book object to display the information of the books.

4.) Modify the availability status of one of the books to reflect that it has been borrowed.

5.) Call the display_info() method on the modified Book object to verify the change in availability status.
Test your implementation by running the Python file and checking the output for correctness.

example output

```
title: "The Catcher in the Rye"
author: "J.D. Salinger"
genre: "Fiction"
available: True | False
```
"""