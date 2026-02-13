#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PicklingError) as e:
            # In a real app, you might log the error: print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from a file using pickle.
        Returns None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
            # In a real app, you might log the error: print(f"Deserialization error: {e}")
            return None