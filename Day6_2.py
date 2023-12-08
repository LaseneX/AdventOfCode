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

# Concatenate individual time values into a string and convert it to an integer
Time = ''
for t in times:
    Time += str(t)
Time = int(Time)

# Concatenate individual distance values into a string and convert it to an integer
Distance = ''
for d in distances:
    Distance += str(d)
Distance = int(Distance)

# Define a function 'f' that calculates a value based on time and distance
def f(time, distance):
    Answer = 0
    # Loop through a range of values based on time
    for x in range(time + 1):
        # Calculate a value 'dx' based on the current 'x' and 'time' values
        distancex = x * (time - x)
        # Check if 'dx' satisfies a condition based on 'distance'
        if distancex >= distance:
            # Increment the counter 'Answer' if the condition is met
            Answer += 1
    return Answer

# Print the result of the function 'f' for the combined Time and Distance values
print(f(Time, Distance))
