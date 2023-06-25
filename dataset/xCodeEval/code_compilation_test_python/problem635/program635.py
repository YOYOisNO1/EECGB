def program635():
    n, m = map(int, input().split())
    days = 0
    i = 1
    while n > 0:
    n -= 1
    days += 1
    if days == m * i:
    n += 1
    i += 1
    print(days)