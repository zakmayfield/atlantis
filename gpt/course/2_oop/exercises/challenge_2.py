"""
Inheritance

You are tasked with extending the Book class in the library system by introducing inheritance. The library now has two types of books - regular books and e-books. E-books have an additional attribute, format, which specifies the format of the e-book (e.g., PDF, EPUB).

Requirements:

1.) Create a class called EBook that inherits from the Book class, which represents an e-book in the library. The EBook class should have the following additional attribute:

- `format`: a string representing the format of the e-book.

2.) Modify the Book class to include a new attribute:

`ebook`: a boolean value representing whether the book is an e-book or not. Set this to False by default.

3.) Modify the display_info() method in the Book class to also display whether the book is an e-book or not, based on the value of the ebook attribute.

4.) Define a new method in the EBook class called display_info() that overrides the display_info() method in the Book class, to display the information of the e-book, including its title, author, genre, availability status, and format.

5.) Instantiate two Book objects and two EBook objects with different attributes to represent four books in the library.

6.) Call the display_info() method on each Book and EBook object to display the information of the books.

7.) Modify the availability status of one of the books to reflect that it has been borrowed.

8.) Call the display_info() method on the modified Book and EBook object to verify the change in availability status.

9.) Test your implementation by running the Python file and checking the output for correctness.
"""
