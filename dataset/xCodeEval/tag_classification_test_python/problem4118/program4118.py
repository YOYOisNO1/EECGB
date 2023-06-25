    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys
    import math
    import random
    import operator
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    from Queue import Queue, PriorityQueue
    from collections import deque, defaultdict, Counter
    getcontext().prec = 100
    
    MOD = 10**9 + 7
    INF = float("+inf")
    
    n, p, t = input().split()
    n = int(n)
    p = float(p)
    t = int(t)
    
    
def prob(n, k, p):
        """nCk(n, k) * p**k * (1-p)**(n-k)"""
        q = 1 - p
        dec = [p] * k + [q] * (n - k) + [1.0 / x for x in range(1, k + 1)]
        inc = range(n, n - k, -1)
    
        res = 1.0
        while inc or dec:
            if (res > 1.0 and dec) or not inc:
                res *= dec[-1]
                del dec[-1]
            else:
                res *= inc[-1]
                del inc[-1]
    
        return res
    
    res = 0.0
    if t <= n:
        for x in xrange(1, n + 1):
            res += x * prob(t, x, p)
    else:
        for x in xrange(1, n):
            res += x * prob(t, x, p)
        for tlast in xrange(n, t + 1):
            res += n * prob(tlast - 1, n - 1, p) * p
    #11234
    print(res)