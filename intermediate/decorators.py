"""
Decorators in Python
Date:
Author:

Learn how to use and create function decorators.
"""

import time
from functools import wraps

# Simple decorator
def my_decorator(func):
    """A basic decorator that prints before and after function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

# Timer decorator
def timer(func):
    """Measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Decorator with arguments
def repeat(times):
    """Repeat function execution multiple times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Using decorators
@my_decorator
def greet(name):
    """Greet someone."""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

@timer
def slow_function():
    """A function that takes some time."""
    time.sleep(0.1)
    return "Done!"

@repeat(3)
def say_hello():
    """Say hello."""
    print("Hello!")

# Main execution
if __name__ == "__main__":
    print("=== Decorator Examples ===\n")
    
    result = greet("Alice")
    print(f"Result: {result}\n")
    
    slow_function()
    print()
    
    say_hello()
