def program7631():
    import math
    
    s = input()
    mod = int(input())
    d = 0
    for i in s:
        d = (d * 10 + int(i)) % mod
    now = d
    l = len(s)
    zz = pow(10, l-1, mod)
    
    for i in xrange(1, l):
        t = int(s[i-1])
        now = ((now - t*zz) * 10 + t) % mod
        if s[i] != '0' and now < d:
            d = now
    print(d)