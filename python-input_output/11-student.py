#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.
    
        If attrs is a list of strings, only attribute names contained in
        this list are retrieved.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student
        instance from a json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
