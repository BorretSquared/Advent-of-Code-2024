import os
import copy

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testinput.txt")

total = 0
loopTotal = 0
uniquePoses = set()
direction = 0  # 0 = north, 1 = east, 2 = south, 3 = west

def rotate():
    global direction
    direction = (direction + 1) % 4

def checkHit(x, y, nestedArray):
    if y < 0 or x < 0 or y >= len(nestedArray) or x >= len(nestedArray[0]):
        return "out_of_range"
    if nestedArray[y][x] == 1:
        return "wall"
    return False

def movement(nestedArray):  # pos movement
    global direction
    pos = [(ix, iy) for ix, row in enumerate(nestedArray) for iy, i in enumerate(row) if i == 2][0]  # find the position of the starting point
    y, x = pos
    for _ in range(4):  # try all four directions
        if direction == 0:
            newX, newY = x, y - 1
        elif direction == 1:
            newX, newY = x + 1, y
        elif direction == 2:
            newX, newY = x, y + 1
        elif direction == 3:
            newX, newY = x - 1, y

        if checkHit(newX, newY, nestedArray) == "out_of_range":
            return None
        if checkHit(newX, newY, nestedArray) != "wall":
            nestedArray[y][x] = 0  # replace old position with a 0
            nestedArray[newY][newX] = 2  # put a 2 in the new position
            return newX, newY
        else:
            rotate()
    return None  # if all directions are blocked, return None

def detectInfiniteLoop(mappedNumbers, blockedX, blockedY):
    global total, uniquePoses, direction

    # Reset global variables
    total = 0
    uniquePoses = set()
    direction = 0

    # Create a copy of the mappedNumbers array
    mappedNumbersCopy = copy.deepcopy(mappedNumbers)

    previousPositions = set()

    # Set the blocked position
    if 0 <= blockedY < len(mappedNumbersCopy) and 0 <= blockedX < len(mappedNumbersCopy[0]):
        mappedNumbersCopy[blockedY][blockedX] = 1

    while True:
        result = movement(mappedNumbersCopy)
        if result is None:
            break
        x, y = result

        # Detect infinite loop
        if (x, y, direction) in previousPositions:
            return True

        previousPositions.add((x, y, direction))
        uniquePoses.add((x, y, direction))
        total = len(uniquePoses)

    return False

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    symbolToNumber = {'.': 0, '#': 1, '^': 2}

    mappedNumbers = []
    for line in lines:
        mappedLine = [symbolToNumber[char] for char in line]
        mappedNumbers.append(mappedLine)

    for y in range(len(mappedNumbers)):
        for x in range(len(mappedNumbers[y])):
            if mappedNumbers[y][x] == 0:
                if detectInfiniteLoop(mappedNumbers, x, y):
                    loopTotal += 1
print(loopTotal)
