def program1716():
    h, n = map(int, input().split())
    n = n - 1 + (1 << h)
    res = h
    for i in range(1, h+1):
        a = n & (1 << i)
        b = n & (1 << (i-1))
        if not ((a == 0) ^ (b == 0)):
            res += (1 << i) - 1
    print(res)