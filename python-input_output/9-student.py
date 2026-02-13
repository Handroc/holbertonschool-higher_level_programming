#!/usr/bin/python3
"""Module defining a basic Student class with JSON output."""

class Student:
    """Represents a student with a JSON-friendly dictionary."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the student."""
        return self.__dict__
