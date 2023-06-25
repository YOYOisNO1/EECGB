def program3855():
    r, h = map(int, input().split())
    p = h / r
    q = h % r
    if 2 * q < r: print 2 * p + 1
    else: print 2 * p + 2