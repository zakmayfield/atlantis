"""
Polymorphism

You are tasked with implementing polymorphism in Python, which is the ability of objects of different classes to respond to the same method or attribute name. Polymorphism allows objects to be treated uniformly, regardless of their specific class, as long as they implement the same interface.

Requirements:

1.) Define a base class called "Shape" that represents a geometric shape. Include attributes for color and size, and create getter and setter methods for each attribute to enforce encapsulation. The getter methods should allow read-only access to the attributes, and the setter methods should allow write-only access to the attributes.

2.) Define a method in the "Shape" class called "area()" that calculates and returns the area of the shape. This method should be overridden by the subclasses.

3.) Instantiate objects of different shape classes that inherit from the "Shape" class, such as "Rectangle", "Circle", and "Triangle". Set different values for the attributes of each shape.

4.) Call the "area()" method on each shape object to calculate and display the area of the shape. Note that the implementation of the "area()" method should be different for each shape class, showcasing polymorphism.

5.) Create a list that contains objects of different shape classes, and iterate over the list, calling the "area()" method on each object. Verify that the correct area is calculated for each shape, regardless of its specific class.

6.) Add additional shape classes that inherit from the "Shape" class, such as "Square" and "Ellipse", and implement the "area()" method for each class according to their respective shapes.

7.) Modify the attributes of the shape objects, such as color and size, using the setter methods, and verify that the changes are reflected in the calculated area.

8.) Test your implementation by running the Python file and checking the output for correctness. Ensure that the correct areas are calculated for different shape objects, and that polymorphism is demonstrated by treating objects of different shape classes uniformly using the "area()" method.
"""
