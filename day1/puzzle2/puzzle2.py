import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
l1, l2 = [], []

# Read and parse input
with open(inputDir) as f:
    for line in f:
        parts = line.split()
        l1.append(int(parts[0]))
        l2.append(int(parts[1]))

# Calculate similarity score
similarityScore = 0
for num in l1:
    similarityScore += num * l2.count(num)

print(similarityScore)
