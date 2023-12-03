import sys
import re
from collections import defaultdict

# Read the file given as an argument to the script
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into lines and create a 2D list (F) to represent the grid
lines = A.split("\n")
F = [[c for c in line] for line in lines]

# Initialize variables
ans = 0  # Variable to store the final answer
nums = defaultdict(list)  # Dictionary to store numbers associated with gear positions

L = len(F)  # Number of rows in the grid
C = len(F[0])  # Number of columns in the grid

# Loop through each row in the grid
for l in range(len(F)):
    gears = set()  # Set to store gear positions
    n = 0  # Variable to store a number being formed
    has_part = False  # Flag to indicate if a non-digit, non-period character is found around a number
    
    # Loop through each character in the row
    for c in range(len(F[l]) + 1):
        # Check if the current character is a digit
        if c < C and F[l][c].isdigit():
            n = n * 10 + int(F[l][c])  # Construct the number from consecutive digits
            
            # Check surrounding characters in a 3x3 grid pattern around the current cell
            for ll in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= l + ll < L and 0 <= c + cc < C:
                        ch = F[l + ll][c + cc]
                        # Check if the surrounding character is not a digit or a period
                        if not ch.isdigit() and ch != '.':
                            has_part = True
                        if ch == '*':
                            gears.add((l + ll, c + cc))  # Store gear position
                        
        elif n > 0:  # If a number has been formed
            for gear in gears:
                nums[gear].append(n)  # Store the number associated with gear positions
            if has_part:
                ans += n  # Add the number to the final answer if it has a non-digit, non-period neighbor
            n = 0
            has_part = False
            gears = set()  # Reset the gear positions

# Print the dictionary containing numbers associated with gear positions
print(nums)

# Reset the 'ans' variable to calculate a new answer
ans = 0

# Loop through the dictionary of gear positions and associated numbers
for k, v in nums.items():
    if len(v) == 2:  # If there are exactly two numbers associated with a gear position
        ans += v[0] * v[1]  # Multiply the two numbers and add to the final answer

# Print the updated final answer
print(ans)
