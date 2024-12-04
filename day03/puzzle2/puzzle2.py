import os
import re
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

mult = []
total = 0
enabled = True
with open(inputDir, 'r') as file:
    content = file.read().replace('\n', '')
    matches = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', content) # terrible regex 
    for match in matches:
        if match[0] == 'do()':
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif enabled and match[1] and match[2]:
            mult.append(int(match[1]) * int(match[2]))

for i in range(len(mult)):
    total += mult[i]

print(total)