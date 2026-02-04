#!/usr/bin/python3
"""Module that defines a VerboseList class inheriting from list."""


class VerboseList(list):
    def append(self, item):
        """Override the append method to print a message."""
        super().append(item)
        print(f"Appending {[item]} to the list")

    def extend(self, items):
        """Override the extend method to print a message."""
        super().extend(items)
        print(f"Extended the list with {[len(items)]} items.")

    def remove(self, item):
        """Override the remove method to print a message."""
        print(f"Removed {[item]} from the list")
        super().remove(item)

    def pop(self, index=-1):
        """Override the pop method to print a message."""
        print(f"Popped {[self[index]]} from the list")
        super().pop(index)
