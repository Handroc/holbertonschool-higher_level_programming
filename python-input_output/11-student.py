#!/usr/bin/python3
"""Module defining a Student class with reloadable JSON data."""


class Student:
    """Represents a student that can reload its attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the student."""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes using a dictionary of values."""
        for i in json:
            if hasattr(self, i):
                setattr(self, i, json[i])
