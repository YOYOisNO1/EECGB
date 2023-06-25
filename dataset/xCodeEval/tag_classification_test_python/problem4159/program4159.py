def program4159():
    h, m, s, t1, t2 = map(int, input().split())
    
    sd = s * 6.0
    md = m * 6.0 + s * 6.0 / 60.0
    hd = h * 30.0 + m * 0.5 + s * 0.5 / 60.0
    arr = [sd, md, hd]
    
    t1 = t1 * 30.0
    t2 = t2 * 30.0
    t1d = min(t1, t2)
    t2d = max(t1, t2)
    
    b1 = True
    b2 = True
    
    for d in arr:
        if d > t1d and d < t2d:
            b2 = False
        else:
            b1 = False
    
    if b1 or b2:
        print('YES')
    else:
        print('NO')