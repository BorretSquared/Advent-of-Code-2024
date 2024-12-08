import os
import copy

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

total = 0
loopTotal = 0
direction = 0  # 0 = north, 1 = east, 2 = south, 3 = west
pos = None

def rotate():
    global direction
    direction = (direction + 1) % 4

def checkHit(x, y, nestedArray):
    if y < 0 or x < 0 or y >= len(nestedArray) or x >= len(nestedArray[0]):
        return "out_of_range"
    return "wall" if nestedArray[y][x] == '#' else False

def movement(nestedArray):
    global pos, direction
    y, x = pos

    for _ in range(4):  # try all four directions
        match direction:
            case 0: newX, newY = x, y - 1
            case 1: newX, newY = x + 1, y
            case 2: newX, newY = x, y + 1
            case 3: newX, newY = x - 1, y

        hitResult = checkHit(newX, newY, nestedArray)
        if hitResult == "out_of_range":
            return None
        if hitResult != "wall":
            # move to new pos
            nestedArray[y][x] = '.'  # replace old pos
            nestedArray[newY][newX] = '^'  # mark new pos
            pos = (newY, newX)  # update pos
            return newX, newY
        else:
            rotate()
    return None  # all directions blocked

def detectInfiniteLoop(mappedNumbers, blockedX, blockedY):
    global direction, pos
    direction = 0 # reset
    # copy
    mappedNumbersCopy = copy.deepcopy(mappedNumbers)
    if 0 <= blockedY < len(mappedNumbersCopy) and 0 <= blockedX < len(mappedNumbersCopy[0]):
        mappedNumbersCopy[blockedY][blockedX] = '#'

    pos = next((ix, iy) for ix, row in enumerate(mappedNumbersCopy) for iy, val in enumerate(row) if val == '^')

    visited_states = set()
    while True:
        current_state = (pos[0], pos[1], direction)
        if current_state in visited_states:
            return True
        visited_states.add(current_state)

        result = movement(mappedNumbersCopy)
        if result is None:
            break
    return False

def findLoops(mappedNumbers):
    global loopTotal
    for y in range(len(mappedNumbers)):
        for x in range(len(mappedNumbers[y])):
            if mappedNumbers[y][x] == '.':  # Check all open positions
                if detectInfiniteLoop(mappedNumbers, x, y):
                    print(f"Loop detected at position ({x}, {y})")
                    loopTotal += 1

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    mappedNumbers = [list(line) for line in lines]

findLoops(mappedNumbers)
print(loopTotal)
