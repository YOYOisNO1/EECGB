    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys
    import math
    import random
    import operator
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    getcontext().prec = 100
    
    MOD = 10**9 + 7
    INF = float("+inf")
    
    n, k, m = map(int, input().split())
    
    if k == 1:
        print (pow(10, n, m) - 1) % m
        quit()
    
    
def pow9_10(x):
        res = 1
        if x > 0:
            res *= 9
        if x > 1:
            res *= pow(10, x - 1, m)
        return res % m
    
    res = 0
    counts = [0] * k
    counts[0] = 1
    
    p10i = 1
    for i in xrange(n):
        counts2 = [0] * k
        for r in xrange(k):
            mind = 1 if i == n else 0
            for d in xrange(mind, 10):
                r2 = (d * p10i + r) % k
                counts2[r2] += counts[r]
    
        add = (counts2[0] - 1) * pow9_10(n - i - 1)
        res += add
    
        counts2[0] = 1
        counts = counts2
    
        p10i = (p10i * 10) % k
    print res % m
    