from collections import defaultdict
import concurrent.futures

inputNums = [int(x) for x in "6563348 67 395 0 6 4425 89567 739318".split()]

def blinkNumbers(numbersWithCounts):
    newCounts = defaultdict(int)
    for num, count in numbersWithCounts.items():
        match num:
            case 0:
                newCounts[1] += count
            case n if n > 9 and len(str(n)) % 2 == 0: # even number of digits & single
                divisor = 10 ** (len(str(n)) // 2)
                left, right = n // divisor, n % divisor # divide number in half
                newCounts[left] += count
                newCounts[right] += count
            case _: # all else
                newCounts[num * 2024] += count
    return newCounts

def blinkMultithreaded(numbersWithCounts, maxWorkers=4):
    # split dict into chunks for parallel processing
    items = list(numbersWithCounts.items())
    chunkSize = len(items) // maxWorkers + (len(items) % maxWorkers > 0)
    chunks = [dict(items[i:i + chunkSize]) for i in range(0, len(items), chunkSize)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
        results = list(executor.map(blinkNumbers, chunks))

    # combine results from all threads
    combinedCounts = defaultdict(int)
    for partialCounts in results:
        for num, count in partialCounts.items():
            combinedCounts[num] += count

    return combinedCounts

# convert to a defaultdict with counts
numbersWithCounts = defaultdict(int)
for num in inputNums:
    numbersWithCounts[num] += 1

for i in range(75):
    numbersWithCounts = blinkMultithreaded(numbersWithCounts)
    totalCount = sum(numbersWithCounts.values())

print(totalCount)
