input_nums = [int(x) for x in "6563348 67 395 0 6 4425 89567 739318".split()]

def blink(numbers):
    result = []
    for num in numbers:
        match num:
            case 0:
                result.append(1)
            case n if n > 9 and len(str(n)) % 2 == 0:
                divisor = 10 ** (len(str(n)) // 2)
                result.extend([n // divisor, n % divisor])
            case _:
                result.append(num * 2024)
    return result
 
count = len(input_nums)
for i in range(75):
    input_nums = blink(input_nums)
    count = len(input_nums)
    print(f"{i}:{count}")

print(count)