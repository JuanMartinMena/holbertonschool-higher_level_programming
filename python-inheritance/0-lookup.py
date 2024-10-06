#!/usr/bin/python3
"""Defines a function to read a text file and print its contents to stdout.

This module provides the function `read_file` that reads a text file
(UTF-8) and prints its contents to the standard output.
"""

def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
