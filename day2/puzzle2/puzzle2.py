import os

inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testinput.txt")
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

def checkValidity(line):
    parts = list(map(int, line.split())) # turn strings into ints
    if sorted(parts) == parts and notDoubleNumber(parts) and distanceDif(parts):
        return True
    elif sorted(parts, reverse=True) == parts and notDoubleNumber(parts) and distanceDif(parts):
        return True
    else:
        return False

def removeOneLineCheck(line): # return true if removing one int lets it pass checkValidity()
    parts = list(map(int, line.split())) # turn strings into ints
    for i in range(len(parts)):
        newParts = parts[:i] + parts[i+1:] # loop through each part and remove one line at a time, then check validity
        if checkValidity(" ".join(map(str, newParts))):
            return True
    return False
    

with open(inputDir) as f:
    for line in f:
        if checkValidity(line) == True:
            total += 1
        elif checkValidity(line) == False and removeOneLineCheck(line) == True:
            total += 1

print(total)