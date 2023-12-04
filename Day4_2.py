import sys
from collections import defaultdict

# Read the file given as an argument to the script
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into lines
lines = A.split('\n')

# Initialize a variable to store the final answer
answer = 0

# Create a defaultdict to track occurrences, initializing with integer values
X = defaultdict(int)

# Iterate through each line in the file with its index
for i, line in enumerate(lines):
    # Increment the count for the current line index in the defaultdict
    X[i] += 1
    
    # Split the line into two parts using '|' as the separator
    z, nums = line.split('|')
    
    # Further split the first part (z) using ':' as the separator
    x, y = z.split(':')
    
    # Convert the 'y' part into a list of integers
    y_nums = [int(l) for l in y.split()]
    
    # Convert the 'nums' part into a list of integers
    numbers = [int(l) for l in nums.split()]
    
    # Find the intersection between the sets of 'y_nums' and 'numbers', count the unique common elements
    value = len(set(y_nums) & set(numbers))
    
    # Update the defaultdict X based on the computed value
    for n in range(value):
        X[i + 1 + n] += X[i]

# Sum all the values in the defaultdict and print the result
print(sum(X.values()))