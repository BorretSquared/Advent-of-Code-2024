import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testinput.txt")

firstNums = []
secondNums = []

with open (inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        firstNums.append(int(line.split(':')[0]))
        secondNums.extend(map(int, line.split(':')[1].split()))
print(firstNums)
print(secondNums)
    