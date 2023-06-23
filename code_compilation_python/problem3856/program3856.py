def program3856():
    r, h = map(int, input().split())
    p = h / r
    q = h % r
    if q > (3. ** 0.5) * r: print 2 * p + 3
    else if 2 * q < r: print 2 * p + 1
    else: print 2 * p + 2