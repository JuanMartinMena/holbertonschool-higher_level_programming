#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None: This function prints the file content and returns nothing.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
