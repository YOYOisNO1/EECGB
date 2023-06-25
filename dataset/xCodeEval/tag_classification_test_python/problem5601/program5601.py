def program5601():
    n, m = sorted(map(int, input().split()))
    
    if n == 1:
        print(m)
    elif n == 2:
        print((m) - m % 4) + 2 * min(m % 4, 2)
    else:
        print((n) * m + 1) / 2