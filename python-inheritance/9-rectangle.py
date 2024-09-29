#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

    def area(self):
        """
        Raises an Exception with the message that area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is an integer greater than zero.

        Args:
            name (str): The name of the parameter to validate.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: String representation in the format [Rectangle]
            <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
