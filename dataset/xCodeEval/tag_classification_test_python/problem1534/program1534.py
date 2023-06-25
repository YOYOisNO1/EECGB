def gcd(p, q):
        while q > 0:
            r = p%q
            p = q
            q = r
        return p
    
def fraction(p, q):
        r = gcd(q, p)
        return '%d/%d' % (p/r, q/r)
    
    a, b, c, d = map(int, input().strip().split())
    bb = b*c
    dd = a*d
    if bb >= dd:
        print(fraction(bb-dd,) bb)
    else:
        print(fraction(dd-bb,) dd)