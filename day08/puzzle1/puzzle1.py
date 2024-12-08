import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

antinodes = {} 
uniquePoints = []

def findDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return y2 - y1, x2 - x1

def checkLegality(x, y, maxX, maxY):
    if not (0 <= x < maxX and 0 <= y < maxY):
        return False
    if [x, y] in [coord for _, coord in uniquePoints]: # _ to ignore first element
        return False
    return True

def addAntinode(x, y):
    if (x, y) in antinodes:
        antinodes[(x, y)] += 1  # Increment count for overlaps
    else:
        antinodes[(x, y)] = 1  # Add new antinode

def display(antinodes, lines):
    grid = [list(line.strip()) for line in lines]
    for x, y in antinodes.keys():
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            grid[y][x] = '#'
    for row in grid:
        print(''.join(row))

with open(inputDir, 'r') as file:
    lines = file.readlines()
    for countY, line in enumerate(lines):
        for countX, point in enumerate(line.strip()):
            if point != '.':
                uniquePoints.append([point, [countX, countY]])
    maxY = len(lines)
    maxX = len(lines[0].strip()) if lines else 0

for i in range(len(uniquePoints)):
    for j in range(i + 1, len(uniquePoints)):
        if uniquePoints[i][0] == uniquePoints[j][0]:
            point1, point2 = uniquePoints[i][1], uniquePoints[j][1]
            dx, dy = findDistance(point1, point2)
            # Calculate possible antinodes
            candidates = [
                (point1[0] - dy, point1[1] - dx),
                (point2[0] + dy, point2[1] + dx)
            ]
            for x, y in candidates:
                if checkLegality(x, y, maxX, maxY):
                    addAntinode(x, y)

display(antinodes, lines)
print(f"Total antinodes: {sum(antinodes.values())}")