def program5330():
    n, m = map(int, input().split())
    c = [0] * (n - 1) + [1, 0]
    for i in range(n - 1, 0, -1):
        fl = 0
        for j in range(2, n // i + 1):
            fl = (fl + c[i * j - 1] - c[min(n, i * j - 1 + j)]) % m
    
        c[i - 1] = (2 * c[i] + fl) % m
    
    print((c[0] - c[1]) % m)