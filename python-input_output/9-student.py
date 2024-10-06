#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
