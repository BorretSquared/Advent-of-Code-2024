import os
import re
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

mult = []
total = 0

with open(inputDir, 'r') as file:
    content = file.read().replace('\n', '')
    matches = re.findall(r'mul\((\d+),(\d+)\)', content)
    for i in range(len(matches)):
        mult.append(int(matches[i][0]) * int(matches[i][1]))
for i in range(len(mult)):
    total += mult[i]

print(total)