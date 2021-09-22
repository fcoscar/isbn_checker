def isbn10_checker(number):
    count = 1
    total = 0
    for i in range(len(number) - 1 ,-1,-1):
        total = int(number[i])*count
        print(f"{number[i]} * {count}")
        count += 1


    return total % 11

