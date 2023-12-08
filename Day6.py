import sys

# Read the contents of the file provided as an argument and remove leading/trailing whitespaces
A = open(sys.argv[1]).read().strip()

# Split the contents of the file into separate lines
lines = A.split('\n')

# Separate time and distance values from the lines
time, distance = lines

# Extract individual time values and convert them to integers
times = [int(x) for x in time.split(':')[1].split()]

# Extract individual distance values and convert them to integers
distances = [int(x) for x in distance.split(':')[1].split()]

# Define a function 'f' that calculates a value based on time and distance
def f(time, distance):
    a = 0
    # Loop through a range of values based on time
    for x in range(time + 1):
        # Calculate a value 'distancex' based on the current 'x' and 'time' values
        distancex = x * (time - x)
        # Check if 'distancex' satisfies a condition based on 'distance'
        if distancex >= distance:
            # Increment the counter 'a' if the condition is met
            a += 1
    return a

# Initialize the variable 'Answer' to 1
Answer = 1

# Loop through each pair of time and distance values
for i in range(len(times)):
    # Calculate the result by multiplying 'Answer' with the result of function 'f' for each pair
    Answer *= f(times[i], distances[i])

# Print the final computed answer
print(Answer)
