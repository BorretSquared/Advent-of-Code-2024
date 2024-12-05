import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

total = 0

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    rules = [line.split('|') for line in lines if '|' in line] # nested array
    updates = [line.split(',') for line in lines if ',' in line] # nested array

    def isOrderCorrect(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update: # loop and see per line if true
                if update.index(rule[0]) > update.index(rule[1]): # check pos's
                    return False
        return True

    correctUpdates = [update for update in updates if isOrderCorrect(update, rules)] # loop through updates, add if in correct order

for update in correctUpdates:
    total += int(update[len(update) // 2]) # find middle
print(total)