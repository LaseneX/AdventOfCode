import sys
from math import gcd

# Read content of the file given as argument
A = open(sys.argv[1]).read().strip()

# Split file content into lines
lines = A.split('\n')
Answer = 0
position = 'AAA'

# Function to calculate the least common multiple (LCM) of a list of numbers
def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // gcd(x, ans)
    return ans

# Splitting the content into LeftRight and Rest parts based on double newlines
LeftRight, Rest = A.split('\n\n')

# Dictionary to store movements for left and right directions
Move = {'L': {}, 'R': {}}

# Extracting movements and options, storing them in Move dictionary
for line in Rest.split('\n'):
    order, options = line.split('=')
    order = order.strip()
    left, right = options.split(',')
    left = left.strip()[1:].strip()  # Removing leading and trailing spaces/characters
    right = right.strip()[:-1].strip()  # Removing leading and trailing spaces/characters
    Move['L'][order] = left
    Move['R'][order] = right

# Function to solve the problem
def solve():
    Positions = []
    # Collect positions that end with 'A'
    for s in Move['L']:
        if s.endswith('A'):
            Positions.append(s)
    Answer = {}
    t = 0
    # Continue iterating until all positions end with 'Z'
    while True:
        IdkWhatToNameThis = []
        # Iterate through positions
        for i, p in enumerate(Positions):
            p = Move[LeftRight[t % len(LeftRight)]][p]  # Move the position according to the given direction
            if p.endswith('Z'):
                Answer[i] = t + 1
                if len(Answer) == len(Positions):
                    return lcm(Answer.values())  # Calculate LCM of values when all positions reach 'Z'
            IdkWhatToNameThis.append(p)
        Positions = IdkWhatToNameThis
        t += 1

# Print the result of the solve function
print(solve())
