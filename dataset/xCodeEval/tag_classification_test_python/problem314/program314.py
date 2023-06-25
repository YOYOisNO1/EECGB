def program314():
    n = int(input())
    count = 0
    if n % 2 == 0:
        count += ((2 + n) // 2) * (n // 2)
        count += ((-1 + -n + 1) // 2) * (n // 2)
    else:
        count += ((-1 + -n) // 2) * (n // 2 + 1)
        count += ((1 + n) // 2) * (n // 2)
    print(count)