import sys

# Reading the file
A = open(sys.argv[1]).read().strip()

# Splitting the contents of the file into parts
parts = A.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

# Class definition for Function
class Function:
    def __init__(own, D):
        lines = D.split('\n')[1:]
        own.tuples = [[int(x) for x in line.split()] for line in lines]

    def apply_one(own, x: int) -> int:
        for (abc, edf, gh) in own.tuples:
            if edf <= x < edf + gh:
                return x + abc - edf
        return x

    def apply_range(own, R):
        G = []
        for (dest, edf, gh) in own.tuples:
            edf_end = edf + gh
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, edf))
                inter = (max(st, edf), min(edf_end, ed))
                after = (max(edf_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    G.append((inter[0] - edf + dest, inter[1] - edf + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return G + R

Fs = [Function(s) for s in others]

# Function f (completed)
def f(R, o):
    G = []
    for line in o:
        dest, edf, gh = [int(x) for x in line.split()]
        edf_end = edf + gh
    return G  

Answer = []
pairs = list(zip(seed[::2], seed[1::2]))

for st, gh in pairs:
    R = [(st, st + gh)]
    for f in Fs:
        R = f.apply_range(R)
    Answer.append(min(R)[0])

print(min(Answer))