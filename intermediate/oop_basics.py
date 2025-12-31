"""
Object-Oriented Programming Basics
Date:
Author:

Learn the fundamentals of OOP in Python: classes, objects, inheritance.
"""

# Basic class
class Dog:
    """A simple Dog class."""
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a Dog instance."""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"
    
    def __str__(self):
        """String representation of the dog."""
        return f"{self.name} is {self.age} years old"


# Inheritance
class GoldenRetriever(Dog):
    """A Golden Retriever is a type of Dog."""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def fetch(self):
        """Golden Retrievers love to fetch."""
        return f"{self.name} loves fetching balls!"


# Using the classes
if __name__ == "__main__":
    print("=== OOP Examples ===\n")
    
    # Create instances
    dog1 = Dog("Buddy", 5)
    dog2 = Dog("Max", 3)
    
    print(dog1)
    print(dog1.bark())
    print(f"Species: {dog1.species}\n")
    
    # Inheritance example
    golden = GoldenRetriever("Charlie", 2, "golden")
    print(golden)
    print(golden.bark())  # Inherited method
    print(golden.fetch())  # New method
