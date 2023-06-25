def program745():
    c, v0, v1, a, l = map(int, input().split())
    
    p, d = v0, 1
    while p < c:
        if v0 + a <= v1: v0 += a
        else: v0 = v1
        p -= l
        if p < 0: p = 0
    
        p += v0
    
        d += 1
    
        if p >= c: break
    
    print(d)