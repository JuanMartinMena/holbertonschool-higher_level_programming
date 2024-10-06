#!/usr/bin/python3
"""
Module for reading a text file.

This module defines a function `read_file` that reads a UTF-8 text
file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
