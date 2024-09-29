#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


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
        self.__integer_validator("width", width)
        self.__integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name: The name of the parameter to validate.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        super().integer_validator(name, value)

