import sys

# Read the file given as an argument to the script
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into lines
lines = A.split('\n')

# Initialize a variable to store the final answer
answer = 0

# Iterate through each line in the file
for line in lines:
    # Split the line into two parts using '|' as the separator
    z, nums = line.split('|')
    
    # Further split the first part (z) using ':' as the separator
    x, y = z.split(':')
    
    # Convert the 'y' part into a list of integers
    y_nums = [int(x) for x in y.split()]
    
    # Convert the 'nums' part into a list of integers
    nums = [int(x) for x in nums.split()]
    
    # Find the intersection between the sets of 'y_nums' and 'nums', count the unique common elements
    value = len(set(y_nums) & set(nums))