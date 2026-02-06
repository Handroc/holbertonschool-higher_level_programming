#!/usr/bin/python3
"""Module that defines a FlyingFish class inheriting from Fish and Bird."""

class Fish:
    def swim(self):
        """Method to simulate swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Method to return the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    def fly(self):
        """Method to simulate flying."""
        print("The bird is flying")

    def habitat(self):
        """Method to return the habitat of the bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        """Method to simulate flying, using the fly method from the Bird class."""
        print("The flying fish is soaring!")

    def swim(self):
        """Method to simulate swimming, using the swim method from the Fish class."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method to return the habitat of the flying fish."""
        print("The flying fish lives in both water and the sky!")