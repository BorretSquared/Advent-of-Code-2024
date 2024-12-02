import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")
total = 0 

def notDoubleNumber(lst): # return true if list has repeating numbers
    seen = set()
    for num in lst:
        if num in seen:
            return False
        seen.add(num)
    return True

def distanceDif(lst): # at least one and at most three backward and forward
    for i in range(len(lst) - 1):
        if abs(lst[i+1] - lst[i]) > 3:
            return False
    return True

with open(inputDir) as f:
    for line in f:
        # split by any whitespace and parse integers
        parts = list(map(int, line.split()))
        if sorted(parts) == parts and notDoubleNumber(parts) and distanceDif(parts):
            total += 1
        elif sorted(parts, reverse=True) == parts and notDoubleNumber(parts) and distanceDif(parts):
            total += 1

print(total)