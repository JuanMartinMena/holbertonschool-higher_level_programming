#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


from rectangle import Rectangle

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
        self.__size = size  # Private attribute
        super().__init__(size, size)
        # Initialize Rectangle with width and height equal to size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area calculation for square

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: Square description.
        """
        return f"[Square] {self.__size}/{self.__size}"  # Square description
