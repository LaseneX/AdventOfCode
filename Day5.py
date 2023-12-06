import sys

# Read the file given as an argument to the script
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into lines
lines = A.split('\n')

# Split the content of the file into parts separated by empty lines
parts = A.split('\n\n')

# Extract the first part after splitting by ':', then split the result into a list of integers
seed, *others = parts
seed = seed.split(':')[1].split()
seed = [int(s) for s in seed]

# Define a function f to process a value 'x' based on the information in a list 'o'
def f(x, o):
    for line in o:
        d, s, r = [int(x) for x in line.split()]
        if s <= x < s + r:
            return d + x - s
    return x

Seeds = []

# Iterate through each value in the 'seed' list
for s in seed:
    s = int(s)
    for o in others:
        O = o.split('\n')
        s = f(s, O[1:])  # Call function 'f' to process 's' with the remaining parts
    Seeds.append(s)

# Find the minimum value in the 'Seeds' list and print it
print(min(Seeds))
