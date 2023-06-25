def program5606():
    n, m = map(int, input().split())
    if min(n, m) <= 1:
        print(n) * m
    elif min(n, m) == 2:
        k = n * m
        tmp = k / 8 * 4
        print(tmp) + min(k - tmp * 2, 4)
    else:
        print((n) * m + 1) / 2
        