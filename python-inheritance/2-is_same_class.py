#!/usr/bin/python3
"""Module that defines a function to read a text file and print its content.

This module contains a function `read_file` that reads a text file
(UTF8) and prints its content to stdout.
"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
