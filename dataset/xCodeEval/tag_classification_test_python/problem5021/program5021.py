def f(W, B):
        n = B - W + 1
        d, p, t, r = [0] * B, [0] * B, [0] * B, [0] * B
    
        p[0], r[0], p[1] = 1, 1, 0.5
        for b in range(2, n + 1):
            d[b] = (t[b - 1] + p[b - 2] * (b - 1)) / (1 + b)
            p[b] = (1 + d[b - 1] * b) / (1 + b)
        r[0], t[0] = 1, 1
        t, r, p = p, t, r
    
        for w in range(2, W):    
            p[1], d[1] = w / (w + 1), 1 / (w + 1)
            for b in range(2, n + w):
                d[b] = ((t[b - 1] * w + p[b - 2] * (b - 1)) * b) / ((w + b) * (w + b - 1))
                p[b] = (w + d[b - 1] * b) / (w + b)
            t, r, p = p, t, r
    
        return t[B - 1]
    
    w, b = map(int, input().split())
    if w == 0: print(0)
    elif b == 0: print(1)
    else: print(f(w + 1, b + 1))