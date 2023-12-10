import sys

# Read content of the file given as argument
A = open(sys.argv[1]).read().strip()

# Split file content into lines
lines = A.split('\n')
Answer = 0

# Function to calculate the cumulative sum based on differences in the provided list
def Function(Xs):
    List = []
    # Calculate differences between consecutive elements in the list
    for i in range(len(Xs) - 1):
        List.append(Xs[i + 1] - Xs[i])
    # If all differences are zero, return the last element of the input list
    if all(y == 0 for y in List):
        return Xs[-1]
    else:
        # Recursively add the last element of the input list and call Function with the calculated differences
        return Xs[-1] + Function(List)

# Iterate through each line in the input
for line in lines:
    # Convert the line into a list of integers
    Xs = [int(x) for x in line.split()]
    # Calculate the result using the Function and add it to the Answer
    Answer += Function(Xs)

# Print the final Answer
print(Answer)
