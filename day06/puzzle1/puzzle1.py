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
    if nestedArray[y][x] == '#':
        return "wall"
    return False

def movement(nestedArray): # pos movement
    global direction
    pos = [(ix, iy) for ix, row in enumerate(nestedArray) for iy, i in enumerate(row) if i == '^'][0] # find the position of the starting point
    y, x = pos
    for _ in range(4):  # try all four directions
        match direction:
            case 0:
                newX, newY = x, y-1
            case 1:
                newX, newY = x+1, y
            case 2:
                newX, newY = x, y+1
            case 3:
                newX, newY = x-1, y
        
        if checkHit(newX, newY, nestedArray) == "out_of_range":
            return None
        if checkHit(newX, newY, nestedArray) != "wall":
            nestedArray[y][x] = '.'  # replace old position with a '.'
            nestedArray[newY][newX] = '^'  # put a '^' in the new position
            return newX, newY
        else:
            rotate()
    return None  # if all directions are blocked, return None

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')

    mappedNumbers = [list(line) for line in lines]

# loop until the next move is out of range
while True:
    result = movement(mappedNumbers)
    if result is None:
        break
    x, y = result
    uniquePoses.add((x, y))
    total = len(uniquePoses)

print("total unique positions visited:", total)