import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
searchedStr = "XMAS"

def countTimes(grid, word):
    rows, cols = len(grid), len(grid[0])
    wordLen = len(word)
    total = 0

    def checkDirection(x, y, dx, dy):
        for k in range(wordLen):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[k]:
                return 0
        return 1
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]: # only check if the first letter matches
                total += checkDirection(i, j, 0, 1) # right
                total += checkDirection(i, j, 0, -1) # left
                total += checkDirection(i, j, 1, 0) # down
                total += checkDirection(i, j, -1, 0) # up
                total += checkDirection(i, j, 1, 1) # down-right
                total += checkDirection(i, j, 1, -1) # down-left
                total += checkDirection(i, j, -1, 1) # up-right
                total += checkDirection(i, j, -1, -1) # up-left
    return total

# read the input
with open(inputDir, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

total = countTimes(lines, searchedStr)
print(total)
