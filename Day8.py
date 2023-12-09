import sys  

# Read content of the file given as argument
A = open(sys.argv[1]).read().strip()

# Split file content into lines
lines = A.split('\n')

# Initialize variables
Answer = 0
position = 'AAA'

# Split the content into LeftRight and Rest parts
LeftRight, Rest = A.split('\n\n')

# Initialize a dictionary to store movements
Move = {'L': {}, 'R': {}}

# Process orders and movements
for line in Rest.split('\n'):
    # Split order and options
    order, options = line.split('=')
    order = order.strip()
    left, right = options.split(',')
    
    # Extract left and right movements, removing leading/trailing spaces
    left = left.strip()[1:].strip()
    right = right.strip()[:-1].strip()
    
    # Store movements in the dictionary for both 'L' and 'R'
    Move['L'][order] = left
    Move['R'][order] = right

# Navigate through movements until reaching 'ZZZ'
while position != 'ZZZ':
    # Determine the movement direction based on LeftRight sequence
    position = Move[LeftRight[Answer % len(LeftRight)]][position]
    Answer += 1  # Increment the step count

# Print the total number of steps taken
print(Answer)
