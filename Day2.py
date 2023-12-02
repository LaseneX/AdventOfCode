import sys

# Read the file
A = open(sys.argv[1]).read().strip()

Answer = 0
# Split every line, every right side of the line and split for every comma
for line in A.split('\n'):
    possible = True
    z, line = line.split(':')
    for x in line.split(';'):
        for balls in x.split(','):
            # Assign the values to compare by using dictionaries
            n, color = balls.split()
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                possible = False
    if possible:
        Answer += int(z.split()[-1])
        print(z)

print(Answer)