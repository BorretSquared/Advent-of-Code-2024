import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
l1, l2 = [], []

def logic(l1, l2):
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    totalDist = 0
    for a, b in zip(l1_sorted, l2_sorted): # combine l1 stored and l2 sorted into 1
        distance = abs(a - b) # get abs of index distances
        totalDist += distance
    return totalDist

# Read and parse input
with open(inputDir) as f:
    for line in f:
        # split by any whitespace and parse integers
        parts = line.split()
        l1.append(int(parts[0]))
        l2.append(int(parts[1]))

# Calculate total distance
totalDist = logic(l1, l2)
print(totalDist)
