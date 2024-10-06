#!/usr/bin/python3
"""Defines a function to create an object from a JSON file.

This module provides the function `load_from_json_file` that reads
a JSON-formatted string from a file and
deserializes it into a Python object.
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str):
        The name of the file to read the JSON object from.

    Returns:
        object: The deserialized Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
