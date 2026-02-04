#!/usr/bin/python3
"""Module that defines an abstract base class."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""
    @abstractmethod
    def sound(self):
        """Abstract method to define the sound of the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a dog, inheriting from Animal."""
    def sound(self):
        """Implementation of the sound method for a dog."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat, inheriting from Animal."""
    def sound(self):
        """Implementation of the sound method for a cat."""
        return "Meow"
