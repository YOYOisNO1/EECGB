def program3222():
    from fractions import gcd
    p = input()
    ans = 0
    for i in xrange(1, p):
        if gcd(i, p - 1) == 1: ans += 1
    print ans