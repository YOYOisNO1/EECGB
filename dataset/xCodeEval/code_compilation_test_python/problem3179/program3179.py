def program3179():
    
     f = lambda: map(int, input().split())
    n, k, m = f()
    p = sorted(f())
    x = 0
    s = sum(p)
    for j in range(n + 1):
        t = m - j * s
        if t < 0: break
        y = k * j + j
        for i in p:
            d = min(n - j, t // i)
            y += d
            t -= d * i
        x = max(x, y)
    print(x)