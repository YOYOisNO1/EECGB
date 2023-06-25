def program3663():
    n, k = map(int, input().split())
    if k == 1:
        print(1)
    if k == 2:
        print(1 + n * (n - 1) // 2)
    if k == 3:
        ##print(1 + n * (n - 1) // 2 * (n - 2))
        print(1 / 0)
    if k == 4:
        print(1 + n * (n - 1) // 2 * (n - 2) * n // (n - 3))
        