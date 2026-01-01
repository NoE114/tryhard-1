"""
Context Managers in Python
Date:
Author:

Learn how to create and use context managers for resource management.
"""

from contextlib import contextmanager
import time

# Creating a context manager with a class
class Timer:
    """A context manager that times code execution."""
    
    def __init__(self, name="Code block"):
        self.name = name
    
    def __enter__(self):
        """Called when entering the 'with' block."""
        self.start = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the 'with' block."""
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"{self.name} took {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

# Creating a context manager with a decorator
@contextmanager
def file_manager(filename, mode):
    """A simple file context manager."""
    print(f"Opening {filename}...")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing {filename}...")
        f.close()

@contextmanager
def suppress_output():
    """Suppress print output within the context."""
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout

# Example usage
if __name__ == "__main__":
    print("=== Context Manager Examples ===\n")
    
    # Using the Timer context manager
    with Timer("Loop execution"):
        total = 0
        for i in range(1000000):
            total += i
        print(f"Sum: {total}")
    
    print()
    
    # Using the file manager
    with file_manager("temp.txt", "w") as f:
        f.write("Hello from context manager!")
    
    with file_manager("temp.txt", "r") as f:
        content = f.read()
        print(f"File content: {content}")
    
    # Clean up
    import os
    os.remove("temp.txt")
    
    print()
    
    # Suppressing output
    print("This will be printed")
    with suppress_output():
        print("This will NOT be printed")
    print("This will be printed again")
