#!/usr/bin/python3
"""Defines a function to return the JSON representation of an object.

This module provides the function `to_json_string` that serializes
an object to a JSON-formatted string.
"""


import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
