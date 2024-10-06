#!/usr/bin/python3
"""Defines a function to write a string to a text file.

This module provides the function `write_file` that writes a string
to a UTF-8 text file and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        Defaults to an empty string.
        text (str): The string to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
