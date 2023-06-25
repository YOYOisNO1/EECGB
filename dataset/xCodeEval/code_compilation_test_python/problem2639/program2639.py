def program2639():
    c, v, v1, a, l = map(int, input().split())
    
    dv = a
    i = 0
    
    while c > 0:
        if i == 1:
            v -= l
            v1 -= l
        i += 1
        c -= v
        l = min(l, c)
        v = min(v1, v + dv)
        dv += a
    
    print(i)
    