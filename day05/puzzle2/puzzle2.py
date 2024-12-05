import os
inputDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")

total = 0

with open(inputDir, 'r') as f:
    lines = f.read().strip().split('\n')
    rules = [line.split('|') for line in lines if '|' in line]  # nested array
    updates = [line.split(',') for line in lines if ',' in line]  # nested array

    def isOrderCorrect(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):  # check positions
                    return False
        return True

    def correctOrder(update, rules):
        update = update[:]  # copy to avoid modifying the original
        reordered = False
        while True:  # recheck until all rules true
            reordered = False
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    idx1, idx2 = update.index(rule[0]), update.index(rule[1]) # indexs
                    if idx1 > idx2:  # wrong
                        # swap elements to correct order
                        update.pop(idx1)
                        update.insert(idx2, rule[0])
                        reordered = True
            if not reordered:  # no changes in pass = break
                break
        if isOrderCorrect(update, rules):  # ensure the order is correct
            return update
        else:
            raise ValueError("cannot change order")

    wrongUpdates = [update for update in updates if not isOrderCorrect(update, rules)]  # find incorrect updates
    wrongUpdatesCorrected = [correctOrder(update, rules) for update in wrongUpdates]

for update in wrongUpdatesCorrected:
    total += int(update[len(update) // 2]) # find middle
print(total)
