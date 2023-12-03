import sys
import re

# Read the file given as an argument to the script
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into lines
lines = A.split("\n")

# Create a 2D list (list of lists) F to represent the grid by converting each line into a list of characters
F = [[c for c in line] for line in lines]

# Initialize a variable to store the final answer
ans = 0

# Get the number of rows (R) and columns (C) in the grid
L = len(F)
C = len(F[0])

# Loop through each row in the grid
for r in range(len(F)):
    # Find numbers in the line using regular expression and print them
    nums = re.findall('-?\d+', lines[r])
    print(nums)
    
    # Initialize variables for number processing
    n = 0
    has_part = False
    
    # Loop through each character in the row
    for c in range(len(F[r]) + 1):
        # Check if the current character is a digit
        if c < C and F[r][c].isdigit():
            n = n * 10 + int(F[r][c])
            
            # Check surrounding characters in a 3x3 grid pattern around the current cell
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < L and 0 <= c + cc < C:
                        ch = F[r + rr][c + cc]
                        # Check if the surrounding character is not a digit or a period
                        if not ch.isdigit() and ch != '.':
                            has_part = True
        elif n > 0:
            # If a number has been formed and there is a non-digit, non-period character around it
            if has_part:
                ans += n
            n = 0
            has_part = False

# Print the final answer
print(ans)
