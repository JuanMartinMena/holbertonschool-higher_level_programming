#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
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
            str: String representation in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size
        super().__init__(size, size)  # Call the parent class with size for both width and height

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: String representation in the format [Rectangle] <size>/<size>.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
