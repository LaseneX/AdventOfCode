import sys

# Read the arguement
A = open(sys.argv[1]).read().strip()
ans = 0

for line in A.split('\n'):
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    score = int(digits[0] + digits[-1])
    ans += score

print(ans)
