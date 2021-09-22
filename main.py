def isbn10_checker(number):
    count = 1
    total = 0
    for i in range(len(number) - 1 ,-1,-1):
        total += int(number[i])*count
        count += 1
    return total % 11 == 0

def isbn13_checker(number):
    count = 0
    total = 0
    for i in range(len(number) - 1 ,-1,-1):
        if count == 1:
            count = 3
        else:
            count = 1
        total += int(number[i]) * count

    print(total)
    return total % 10 == 0