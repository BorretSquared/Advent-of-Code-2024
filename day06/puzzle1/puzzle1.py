import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

total = 0
uniquePoses = set()
direction = 0 # 0 = north, 1 = east, 2 = south, 3 = west

def rotate():
    global direction
    direction = (direction + 1) % 4

def checkHit(x, y, nestedArray):
    if y < 0 or x < 0 or y >= len(nestedArray) or x >= len(nestedArray[0]):
        return "out_of_range"
    if nestedArray[y][x] == 1:
        return "wall"
    return False

def movement(nestedArray): # pos movement
    global direction
    pos = [(ix, iy) for ix, row in enumerate(nestedArray) for iy, i in enumerate(row) if i == 2][0] # find the position of the starting point
    y, x = pos
    for _ in range(4):  # try all four directions
        if direction == 0:
            newX, newY = x, y-1
        elif direction == 1:
            newX, newY = x+1, y
        elif direction == 2:
            newX, newY = x, y+1
        elif direction == 3:
            newX, newY = x-1, y
        
        if checkHit(newX, newY, nestedArray) == "out_of_range":
            return None
        if checkHit(newX, newY, nestedArray) != "wall":
            nestedArray[y][x] = 0  # replace old position with a 1
            nestedArray[newY][newX] = 2  # put a 2 in the new position
            return newX, newY
        else:
            rotate()
    return None  # if all directions are blocked, return None

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    symbolToNumber = {'.': 0, '#': 1, '^': 2}

    mappedNumbers = []
    for line in lines:
        mappedLine = [symbolToNumber[char] for char in line]
        mappedNumbers.append(mappedLine)

# loop until the next move is out of range
while True:
    result = movement(mappedNumbers)
    if result is None:
        break
    x, y = result
    uniquePoses.add((x, y))
    total = len(uniquePoses)

print("total unique positions visited:", total)

# display path
outputArray = [['.' if cell == 0 else '#' for cell in row] for row in mappedNumbers]
for x, y in uniquePoses:
    outputArray[y][x] = 'X'
for row in outputArray:
    print(''.join(row))
# comment to get to line 69