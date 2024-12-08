import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

total = 0

def solve(nums, ops): # in order L->R
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        elif ops[i] == '*':
            result *= nums[i+1]
        elif ops[i] == '|': # combine digits w/ conocatenation
            result = int(str(result) + str(nums[i+1]))
    return result

def generateCombos(n):
    if n == 0:
        return [[]]
    smallerCombos = generateCombos(n-1)
    combos = []
    for combo in smallerCombos:
        for op in '+*|': # try all combos
            newCombo = combo + [op]
            combos.append(newCombo)
    return combos

def checkValidity(targetNum, nums):
    for ops in generateCombos(len(nums)-1):
        if solve(nums, ops) == targetNum: # loop through combos until 1 is found
            return True
    return False

with open(inputDir, 'r') as file:
    for line in file:
        targetNum, nums = line.split(':')
        targetNum = int(targetNum.strip())
        nums = list(map(int, nums.strip().split()))
        if checkValidity(targetNum, nums):
            total += targetNum
print(total)
