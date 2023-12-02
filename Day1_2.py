import sys

A = open(sys.argv[1]).read().strip()
total = 0

for line in A.split('\n'):
    numbers = []
    for i, c in enumerate(line):
        if c.isdigit():
            numbers.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                numbers.append(str(d+1))
    total += int(numbers[0] + numbers[-1])

print(total)
