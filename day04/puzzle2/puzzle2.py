import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
searchedStr1 = "MAS"
searchedStr2 = "SAM"

def countTimes(grid, word1, word2):
    rows, cols = len(grid), len(grid[0])
    total = 0

    def checkDiagonals(x, y):
        if (x - 1 >= 0 and y - 1 >= 0 and x + 1 < rows and y + 1 < cols and
            ((grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1] in [word1, word2]) and
             (grid[x+1][y-1] + grid[x][y] + grid[x-1][y+1] in [word1, word2]))):
            return 1
        return 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A': # only check if the middle letter is 'A'
                total += checkDiagonals(i, j)
    return total

# read the input
with open(inputDir, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

total = countTimes(lines, searchedStr1, searchedStr2)
print(total)
