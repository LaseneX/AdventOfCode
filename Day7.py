import sys
from collections import Counter

# Read content of the file given as argument
A = open(sys.argv[1]).read().strip()

# Split file content into lines
lines = A.split('\n')
Answer = 0

# Function to evaluate the strength of a poker hand
def strength(hand):
    # Replace card ranks with numeric values
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    # Count occurrences of each card rank in the hand
    counter = Counter(hand)

    # Evaluate strength of the hand based on occurrences
    if sorted(counter.values()) == [5]:
        return (10, hand)
    # Other elif conditions for different poker hand strengths...
    else:
        assert False, f'{counter} {hand} {sorted(counter.values())}'

# Store hands and bets in a list of tuples
Hands = []
for line in lines:
    hand, bet = line.split()
    Hands.append((hand, bet))

# Sort hands based on their strengths
Hands = sorted(Hands, key=lambda hb: strength(hb[0]))

# Calculate the score based on hand strength and associated bet
for i, (h, b) in enumerate(Hands):
    Answer += (i + 1) * int(b)

# Print the final calculated answer
print(Answer)
