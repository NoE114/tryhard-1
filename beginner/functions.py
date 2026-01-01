"""
Functions in Python
Date:
Author:

Learn how to create and use functions to organize your code.
"""

# Basic function
def greet():
    """Simple function that prints a greeting."""
    print("Hello from a function!")

# Function with parameters
def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

# Function with default parameters
def introduce(name, age=0):
    """Introduce a person with optional age."""
    if age > 0:
        print(f"Hi, I'm {name} and I'm {age} years old.")
    else:
        print(f"Hi, I'm {name}.")

# Function with multiple return values
def get_stats(numbers):
    """Return min, max, and average of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Main execution
if __name__ == "__main__":
    print("=== Function Examples ===\n")
    
    # Call basic function
    greet()
    
    # Call function with parameter
    greet_person("Alice")
    
    # Use return value
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    # Use default parameters
    introduce("Bob")
    introduce("Charlie", 25)
    
    # Multiple return values
    nums = [1, 2, 3, 4, 5]
    minimum, maximum, average = get_stats(nums)
    print(f"\nStats for {nums}:")
    print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")
