    #!/usr/bin/env python
    # coding: utf-8
    
def ternary(n):
        res = []
        while n > 0:
            res.append(n % 3)
            n /= 3
        return res
    
def decimal(t):
        res = 0
        for i in reversed(t):
            res *= 3
            res += i
        return res
    
    a, c = [int(s) for s in input().split()]
    ta, tc = ternary(a), ternary(c)
    while len(ta) < len(tc):
        ta.append(0)
    while len(ta) > len(tc):
        tc.append(0)
    tb = ta[:]
    for i in range(len(ta)):
        n = tc[i] - ta[i]
        if n < 0:
            n += 3
        tb[i] = n
    print(decimal(tb))