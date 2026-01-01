"""
File Handling in Python
Date:
Author:

Learn different ways to read and write files in Python.
"""

import json
import csv
from pathlib import Path

# Get the directory of this script
SCRIPT_DIR = Path(__file__).parent

# Writing and reading text files
def text_file_example():
    """Demonstrate basic text file operations."""
    print("=== Text File Operations ===")
    
    file_path = SCRIPT_DIR / "sample.txt"
    
    # Writing to a file
    with open(file_path, "w") as f:
        f.write("Hello, World!\n")
        f.write("This is a text file.\n")
        f.write("Python makes file handling easy!")
    
    # Reading from a file
    with open(file_path, "r") as f:
        content = f.read()
        print("File content:")
        print(content)
    
    # Reading line by line
    print("\nReading line by line:")
    with open(file_path, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")
    
    # Clean up
    file_path.unlink()

# JSON file operations
def json_file_example():
    """Demonstrate JSON file operations."""
    print("\n=== JSON File Operations ===")
    
    file_path = SCRIPT_DIR / "data.json"
    
    # Data to save
    data = {
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "JavaScript", "SQL"]
    }
    
    # Writing JSON
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    
    # Reading JSON
    with open(file_path, "r") as f:
        loaded_data = json.load(f)
        print(f"Loaded data: {loaded_data}")
    
    # Clean up
    file_path.unlink()

# CSV file operations
def csv_file_example():
    """Demonstrate CSV file operations."""
    print("\n=== CSV File Operations ===")
    
    file_path = SCRIPT_DIR / "data.csv"
    
    # Writing CSV
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 25, "NYC"])
        writer.writerow(["Bob", 30, "LA"])
    
    # Reading CSV
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
    # Clean up
    file_path.unlink()

# Main execution
if __name__ == "__main__":
    text_file_example()
    json_file_example()
    csv_file_example()
    
    print("\n✓ All file operations completed successfully!")
