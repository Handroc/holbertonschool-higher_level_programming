#!/usr/bin/python3
"""Module defining a Student class with filtered JSON output."""


class Student:
    """Represents a student with optional attribute filtering."""
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
