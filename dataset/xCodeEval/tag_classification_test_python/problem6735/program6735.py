def program6735():
    gcd = lambda a, b: gcd(b, a%b) if b else a
    la, ra, ta = map(int, input().split())
    lb, rb, tb = map(int, input().split())
    d = gcd(ta, tb)
    if la > lb:
    	la, lb = lb, la
    	ra, rb = rb, ra
    diff = d * ((lb - la) / d)
    la += diff
    ra += diff
    res = min(ra, rb) - max(la, lb)
    la += d
    ra += d
    res = max(res, min(ra, rb) - max(la, lb))
    if ra > rb:
    	la, lb = lb, la
    	ra, rb = rb, ra
    diff = d * ((rb - ra+1) / d)
    la += diff
    ra += diff
    res = max(res, min(ra, rb) - max(la, lb))
    la += d
    ra += d
    res = max(res, min(ra, rb) - max(la, lb))
    print(max(0,) res+1)