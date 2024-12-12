import os

input =  open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")).read().strip().split('\n')
input = [list(map(int, list(line))) for line in input]

def findTrailheadScores(topographicMap):
    def isValid(x, y):
        return 0 <= x < rows and 0 <= y < cols and (x, y) not in visited

    def bfsTrailhead(startX, startY):
        queue = [(startX, startY)]
        visitedInBfs = set()
        visitedInBfs.add((startX, startY))

        reachableNines = set()
        while queue:
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if isValid(nx, ny) and (nx, ny) not in visitedInBfs:
                    if topographicMap[nx][ny] == topographicMap[x][y] + 1:
                        visitedInBfs.add((nx, ny))
                        queue.append((nx, ny))
                        if topographicMap[nx][ny] == 9:
                            reachableNines.add((nx, ny))

        return len(reachableNines)

    rows = len(topographicMap)
    cols = len(topographicMap[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    visited = set()
    totalScore = 0

    for i in range(rows):
        for j in range(cols):
            if topographicMap[i][j] == 0 and (i, j) not in visited:
                score = bfsTrailhead(i, j)
                totalScore += score
                visited.add((i, j))

    return totalScore
print(findTrailheadScores(input))
