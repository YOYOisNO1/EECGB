def program721():
    k, b, n, t = map(int, input().split())
    p = 1
    while p <= t:
        p = k * p + b
        n -= 1
    print(max(0, n+1))