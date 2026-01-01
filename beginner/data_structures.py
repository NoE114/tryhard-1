"""
Data Structures - Lists, Tuples, Dictionaries, Sets
Date:
Author:

Learn about Python's built-in data structures.
"""

# Lists - ordered, mutable
print("=== Lists ===")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
fruits.append("orange")  # Add item
print(f"After append: {fruits}")
fruits[1] = "blueberry"  # Modify item
print(f"After modification: {fruits}")

# List operations
numbers = [1, 2, 3, 4, 5]
print(f"\nNumbers: {numbers}")
print(f"First: {numbers[0]}, Last: {numbers[-1]}")
print(f"Slice [1:3]: {numbers[1:3]}")
print(f"Length: {len(numbers)}")

# Tuples - ordered, immutable
print("\n=== Tuples ===")
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
x, y = coordinates  # Unpacking
print(f"x={x}, y={y}")

# Dictionaries - key-value pairs
print("\n=== Dictionaries ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")
print(f"Name: {person['name']}")
person["email"] = "alice@example.com"  # Add new key
print(f"After adding email: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# Sets - unordered, unique elements
print("\n=== Sets ===")
colors = {"red", "green", "blue"}
print(f"Colors: {colors}")
colors.add("yellow")
print(f"After adding: {colors}")
colors.add("red")  # Duplicates are ignored
print(f"After adding duplicate: {colors}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet1: {set1}, Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
