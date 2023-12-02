import sys
from collections import defaultdict

# Read the file
A = open(sys.argv[1]).read().strip()

Answer = 0
# Split every line, every right side of the line and split for every comma
for line in A.split('\n'):
    # Z is Game: side
    z, line = line.split(':')
    # defaultdict solves missing key issue
    X = defaultdict(int)
    for x in line.split(';'):
        for balls in x.split(','):
            # n is number and color is the color
            n, color = balls.split()
            n = int(n)
            # Pick the highest values
            X[color] = max(X[color], n)
    points = 1
    for x in X.values():
        points *= x
    Answer += points
print(Answer)