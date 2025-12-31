"""
List and Dictionary Comprehensions
Date:
Author:

Learn powerful one-line expressions for creating lists and dictionaries.
"""

# List comprehension basics
print("=== List Comprehensions ===")

# Traditional way
squares_traditional = []
for i in range(10):
    squares_traditional.append(i ** 2)
print(f"Traditional: {squares_traditional}")

# List comprehension way
squares = [i ** 2 for i in range(10)]
print(f"Comprehension: {squares}")

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehensions
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehensions
print("\n=== Dictionary Comprehensions ===")

# Create a dictionary from lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = {k: v for k, v in zip(keys, values)}
print(f"Person: {person}")

# Square numbers
square_dict = {x: x ** 2 for x in range(5)}
print(f"Squares: {square_dict}")

# Filter dictionary
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 68}
passing = {name: score for name, score in scores.items() if score >= 75}
print(f"Passing scores: {passing}")

# Set comprehensions
print("\n=== Set Comprehensions ===")
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "date"]}
print(f"Unique word lengths: {unique_lengths}")

# Generator expressions (memory efficient)
print("\n=== Generator Expressions ===")
sum_of_squares = sum(i ** 2 for i in range(1000))
print(f"Sum of squares (0-999): {sum_of_squares}")
