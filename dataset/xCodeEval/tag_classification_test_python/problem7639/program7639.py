def program7639():
    a, b, p, x = map(int, input().strip().split())
    a = pow(a, p - 2, p)
    
    d = {}
    for r in xrange(p - 1):
        s = b * pow(a, r, p) % p
        res = (s + ((r - s) % (p - 1)) * p) % (p * (p - 1))
    
        try: d[res] += 1
        except: d[res] = 1
    
    ans = 0
    Q = x // (p * (p - 1))
    R = x % (p * (p - 1))
    
    for r in d:
        if r <= R: ans += (Q + 1)
        else: ans += Q
    
    print(ans)