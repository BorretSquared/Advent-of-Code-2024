import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testinput.txt")

total = 0
uniquePoints = set() # allow for adding
uniquePointPositions = []

with open(inputDir, 'r') as file:
    for line in file:
        points = line.strip().split()
        for point in points:
            if point != '.':
                print(point)
                uniquePoints.add(point)
