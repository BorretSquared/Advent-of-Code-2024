import os

def get_unique_positions(inputDir):
    total = 0
    uniquePoses = set()
    direction = 0  # 0 = north, 1 = east, 2 = south, 3 = west
    pos = None

    def rotate():
        nonlocal direction
        direction = (direction + 1) % 4

    def checkHit(x, y, nestedArray):
        if y < 0 or x < 0 or y >= len(nestedArray) or x >= len(nestedArray[0]):
            return "out_of_range"
        return "wall" if nestedArray[y][x] == '#' else False

    def movement(nestedArray):
        nonlocal pos, direction
        y, x = pos

        for _ in range(4): # try all four directions
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
                nestedArray[y][x] = '.' # replace old pos
                nestedArray[newY][newX] = '^' # mark new pos
                pos = (newY, newX) # update pos
                return newX, newY
            else:
                rotate()
        return None # all directions blocked

    with open(inputDir, 'r') as f:
        lines = f.read().strip().split('\n')
        mappedNumbers = [list(line) for line in lines]

    pos = next((ix, iy) for ix, row in enumerate(mappedNumbers) for iy, val in enumerate(row) if val == '^')

    while True:
        result = movement(mappedNumbers)
        if result is None:
            break
        x, y = result
        uniquePoses.add((x, y))
        total = len(uniquePoses)

    return uniquePoses

if __name__ == "__main__":
    inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
    unique_positions = get_unique_positions(inputDir)
    print("Total unique positions visited:", len(unique_positions))
