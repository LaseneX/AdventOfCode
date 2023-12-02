import sys

# Read the file
A = open(sys.argv[1]).read().strip()

# Sum of all numbers
total = 0

# For every new line
for line in A.split('\n'):
    # Create a list and empty it at the end of every for loop
    numbers = []
    # Find the numbers
    for i, c in enumerate(line):
        if c.isdigit():
            # We add every digit we find
            numbers.append(c)
        # We check for every string number and add them to list 
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                numbers.append(str(d+1))
    # Merge the first and final digit and add it to sum
    total += int(numbers[0] + numbers[-1])

# Final answer
print(total)
