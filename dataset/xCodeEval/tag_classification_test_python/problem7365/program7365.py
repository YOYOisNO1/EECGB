def program7365():
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    if n == 1:
        a = [0, 1, 2, 3, 2, 1]
        print(m) - a[m%6]
    elif m <= 2:
        print(0)
    elif n == 2:
        if m == 3 or m == 7:
            print(n) * m - 2
        else:
            print(n) * m
    elif n % 2:
        print(n) * m - (n * m) % 2
    else:
        print(n) * m