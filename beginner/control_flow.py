"""
Control Flow - Conditional Statements and Loops
Date:
Author:

Learn how to control program flow with if/else and loops.
"""

# If/Elif/Else statements
print("=== Conditional Statements ===")
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm!")
elif temperature > 10:
    print("It's cool!")
else:
    print("It's cold!")

# For loops
print("\n=== For Loops ===")
# Loop through a range
for i in range(5):
    print(f"Count: {i}")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loops
print("\n=== While Loops ===")
count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1

# Break and continue
print("\n=== Break and Continue ===")
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(f"Number: {i}")

# Nested loops
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after inner loop
