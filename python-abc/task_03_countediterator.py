#!/usr/bin/python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    def __init__(self, iterator):
        """Initialize the CountedIterator with an iterator."""
        self.iterator = iter(iterator)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def get_count(self):
        """Return the number of items returned so far."""
        return self.count

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item
