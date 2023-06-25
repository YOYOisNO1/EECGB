def program1507():
    n, k = [ int(i) for i in input().split() ]
    p = int((8 * n + 8 * k + 9) ** 0.5)
    print((3 + 2 * n - p) // 2)