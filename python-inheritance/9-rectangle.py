#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)  # Use the inherited method to validate
        self.integer_validator("height", height)  # Use the inherited method to validate
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height  # Area calculation

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: Rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"  # String representation
