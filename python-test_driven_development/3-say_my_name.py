#!/usr/bin/python3
"""
Module: 3-say_my_name

This module contains a single function that prints the name provided by the user.
The function ensures that both the first name and last name are strings before
printing the formatted name

Function:
    - say_my_name: Prints "My name is <first_name> <last_name>" if inputs are valid.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
