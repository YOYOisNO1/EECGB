def program565():
    n, m, a, b = [int(x) for x in input().split()]
    print(min((n - n // m * m) * b, ((n // m + 1) * m - n) * a))