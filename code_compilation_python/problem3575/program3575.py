def program3575():
    import sys
    a, b, w, x, c = map(int, input().split())
    if c <= a:
        print(0)
        sys.exit()
    d = c - a
    ans = 0
    if b // x >= d:
        print(d)
        sys.exit()
    ans += (b // x + 1) 
    d -= (b // x)
    b = w - (x - b % x)
    b0 = b
    g = 0
    det = 0
    while (1):
        if b // x >= d:
            print(ans + d)
            sys.exit()
        g += (b // x + 1)
        det += (b // x)
        ans += (b // x + 1)
        d -= (b // x)
        b = w - (x - b % x)
        if b == b0:
            break
    
    ans += (d // det) * g
    d %= det
    if d == 0:
        print(ans - 1)
        sys.exit()
    while (1):
        if b // x >= d:
            print(ans + d)
            sys.exit()
        ans += (b // x + 1)
        d -= (b // x)
        b = w - (x - b % x)