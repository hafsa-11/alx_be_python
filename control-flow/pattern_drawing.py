#!/usr/bin/env python3

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop (while) for each row
while row < size:
    # Inner loop (for) for each column
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
