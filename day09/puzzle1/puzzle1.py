import os
inputNumber = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "input.txt")).readline().strip()
diskMap = str(inputNumber)
result = []
fileId = 0

i = 0
while i < len(diskMap):
    fileLength = int(diskMap[i])
    result.extend([str(fileId)] * fileLength)
    i += 1
    if i < len(diskMap):
        freeSpaceLength = int(diskMap[i])
        result.extend(['.'] * freeSpaceLength)
        i += 1
    fileId += 1

print(''.join(result))
while '.' in result:
    print(''.join(result))
    dotIndex = result.index('.')
    for i in range(len(result) - 1, dotIndex, -1):
        if result[i] != '.':
            result[dotIndex], result[i] = result[i], '.'
            break
    else:
        allDotsAfter = all(char == '.' for char in result[dotIndex:])
        noDotsBefore = all(char != '.' for char in result[:dotIndex])
        if allDotsAfter and noDotsBefore:
            break
checksum = 0
for position, block in enumerate(result):
    if block != '.':
        checksum += position * int(block)

print(checksum)