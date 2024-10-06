#!/usr/bin/python3
"""Defines a function to save an object
to a text file using JSON representation.

This module provides the function `save_to_json_file` that serializes
an object to a JSON-formatted string and writes it to a file.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
