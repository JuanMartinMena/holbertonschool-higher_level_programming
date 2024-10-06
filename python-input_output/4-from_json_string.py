#!/usr/bin/python3
"""Defines a function to return an object represented
by a JSON string.

This module provides the function `from_json_string`
that deserializes
a JSON-formatted string to a Python object.
"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
