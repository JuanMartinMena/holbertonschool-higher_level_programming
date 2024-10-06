#!/usr/bin/python3
class Student:
    """
    A class that defines a student by their first name, last name, and age.
    """


    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary containing the specified attributes of the student
                  or all attributes if attrs is None.
        """
        if attrs is None:
            return self.__dict__
        
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values from the provided dictionary.

        Args:
            json (dict): A dictionary containing the new values for the attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
