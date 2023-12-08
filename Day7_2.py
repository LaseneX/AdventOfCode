import sys
from collections import Counter

# Read content of the file given as argument and strip any leading/trailing whitespaces
A = open(sys.argv[1]).read().strip()

# Split file content into lines
lines = A.split('\n')

# Function to evaluate the strength of a poker hand
def strength(hand, x):
    # Replace card ranks with numeric values
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    # Count occurrences of each card rank in the hand
    counter = Counter(hand)

    # Manipulate the hand based on a condition (if x is True)
    if x:
        target = list(counter.keys())[0]
        # Logic to find the most occurring non-'1' card rank
        for c in counter:
            if c != '1':
                if counter[c] > counter[target] or target == '1':
                    target = c
        # Assertions to ensure correct conditions
        assert target != '1' or list(counter.keys()) == ['1']
        if '1' in counter and target != '1':
            counter[target] += counter['1']
            del counter['1']
        assert '1' not in counter or list(counter.keys()) == ['1'], f'{counter} {hand}'

    # Evaluate strength of the hand based on occurrences
    if sorted(counter.values()) == [5]:
        return (10, hand)
    # Other elif conditions for different poker hand strengths...
    else:
        assert False, f'{counter} {hand} {sorted(counter.values())}'

# Loop to evaluate hands in two different conditions (False and True)
for x in [False, True]:
    Hands = []
    # Iterate through lines and evaluate hand strengths
    for line in lines:
        hand, bet = line.split()
        Hands.append((hand, bet))
        Hands = sorted(Hands, key=lambda hb: strength(hb[0], x))
        Answer = 0
        # Calculate score based on hand strength and associated bet
        for i, (h, b) in enumerate(Hands):
            Answer += (i + 1) * int(b)
# Print the final calculated answer (outside the loop, so it's only printed once)
print(Answer)