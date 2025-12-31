"""
Variables and Data Types in Python
Date:
Author:

Learn about different data types and how to work with variables.
"""

# Integer
age = 25
print(f"Age: {age} (type: {type(age).__name__})")

# Float
height = 5.9
print(f"Height: {height} (type: {type(height).__name__})")

# String
name = "Python Learner"
print(f"Name: {name} (type: {type(name).__name__})")

# Boolean
is_learning = True
print(f"Learning: {is_learning} (type: {type(is_learning).__name__})")

# Type conversion
age_str = str(age)
height_int = int(height)
print(f"\nConverted age to string: '{age_str}'")
print(f"Converted height to int: {height_int}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Constants (by convention, use uppercase)
PI = 3.14159
MAX_SIZE = 100
print(f"\nConstants: PI={PI}, MAX_SIZE={MAX_SIZE}")
