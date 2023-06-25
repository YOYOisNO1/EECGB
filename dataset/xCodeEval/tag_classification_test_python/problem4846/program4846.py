def program4846():
    n, s = map(int, input().split())
    if s <= n:
        print(1)
    else:
        print((s + n - 1) // n)