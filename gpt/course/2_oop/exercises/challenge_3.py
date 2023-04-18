"""
You are tasked with implementing encapsulation for a class in Python. Encapsulation is a mechanism that restricts the access to certain class attributes or methods, ensuring that they can only be accessed within the class or its subclasses, and not from outside the class.

Requirements:

1.) Create a class called "Person" that represents a person's information, such as their name, age, and address. Include attributes for name, age, and address, and create getter and setter methods for each attribute to enforce encapsulation. The getter methods should allow read-only access to the attributes, and the setter methods should allow write-only access to the attributes.

2.) Define a method in the "Person" class called "display_info()" that displays the information of the person, including their name, age, and address.

3.) Instantiate an object of the "Person" class with some initial values for the attributes.

4.) Call the "display_info()" method on the "Person" object to display the information of the person.

5.) Attempt to directly access or modify the attributes of the "Person" object from outside the class, and verify that it raises an error due to encapsulation.

6.) Define a subclass of the "Person" class called "Employee" that inherits from the "Person" class.

7.) Add additional attributes to the "Employee" class, such as job title, salary, and employee ID, and create getter and setter methods for these attributes to enforce encapsulation.

8.) Define a method in the "Employee" class called "display_info()" that overrides the "display_info()" method in the "Person" class, to display the information of the employee, including their name, age, address, job title, salary, and employee ID.

9.) Instantiate an object of the "Employee" class with some initial values for the attributes.

10.) Call the "display_info()" method on the "Employee" object to display the information of the employee, including the inherited attributes from the "Person" class.

11.) Attempt to directly access or modify the attributes of the "Employee" object from outside the class, and verify that it raises an error due to encapsulation.

12.) Test your implementation by running the Python file and checking the output for correctness.
"""
