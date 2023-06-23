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
    
    
def count_div_upto_pow10(e, kk):
        q, r = divmod(pow(10, e), kk)
        if r == 0:
            q -= 1
        return q
    
    
def count_div_interval(e1, e2, kk):
        return count_div_upto_pow10(e2, kk) - count_div_upto_pow10(e1, kk)
    
    
def cut_pow10(e):
        return pow(10, e) if e > 0 else 1
    
    res = 0
    counts = {r: 0 for r in xrange(k)}
    counts[0] = 1
    
    for i in xrange(n):
        #print i, ":",
        p10 = pow(10, i)
    
        counts2 = {r: 0 for r in xrange(k)}
        for r in xrange(k):
            mind = 1 if i == n else 0
            for d in xrange(mind, 10):
                r2 = (d * pow(10, i, k) + r) % k
                counts2[r2] += counts[r]
        #print counts2
        add = (counts2[0] - 1) * pow9_10(n - i - 1)
        res += add
        #print "ADD", counts2[0], "*", pow9_10(n - i - 1), "=", add
        counts2[0] = 1
        counts = counts2
    print res % m
    