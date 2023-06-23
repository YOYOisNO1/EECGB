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
    
    n = int(input())
    rmax = 0
    intervals = []
    for _ in xrange(n):
        l, r = map(int, input().split())
        rmax = max(rmax, r)
        intervals.append((l, r))
    
    
def prob_smaller_equal(ints, val):
        res = 1.0
        for l, r in ints:
            d = min(val + 1 - l, r + 1 - l)
            if d <= 0:
                return 0.0
            res *= float(d) / (r + 1 - l)
            if res == 0.0:
                return 0.0
        return res
    
    
def prob_smaller(ints, val):
        res = 1.0
        for l, r in ints:
            d = min(val - l, r + 1 - l)
            if d <= 0:
                return 0.0
            res *= float(d) / (r + 1 - l)
            if res == 0.0:
                return 0.0
        return res
    
    
def prob_greater(ints, val):
        res = 1.0
        for l, r in ints:
            d = min(r - val, r + 1 - l)
            if d <= 0:
                return 0.0
            res *= float(d) / (r + 1 - l)
            if res == 0.0:
                return 0.0
        return res
    
    
def prob_equal(ints, val):
        res = 1.0
        for l, r in ints:
            if not (l <= val <= r):
                return 0.0
            res *= 1.0 / (r + 1 - l)
        return res
    
    
def combos(ints, minn, maxn):
        for ntie in xrange(minn, maxn + 1):
            for ints_tie in combinations(ints, r=ntie):
                yield ints_tie
    
    INTINDS = range(len(intervals))
    res = 0
    for i_int1 in INTINDS:
        for i_ints2_tie in combos(INTINDS, 1, n - 1):
            if i_int1 in i_ints2_tie:
                continue
            i_other = [i for i in INTINDS if i not in i_ints2_tie and i != i_int1]
    
            int1 = intervals[i_int1]
            ints2_tie = [intervals[i] for i in i_ints2_tie]
            other = [intervals[i] for i in i_other]
    
            for price in xrange(1, rmax + 1):
                add = prob_smaller(other, price) * prob_equal(ints2_tie, price) * prob_greater([int1], price)
                # if add:
                    # print int1, " | ", ints2_tie, " : ", "price2", price, "*", add, "=", add * price
                res += add * price
    
    # print
    
    for i_ints1_tie in combos(INTINDS, 2, n):
        i_other = [i for i in INTINDS if i not in i_ints1_tie]
    
        ints1_tie = [intervals[i] for i in i_ints1_tie]
        other = [intervals[i] for i in i_other]
        for price in xrange(1, rmax + 1):
            add = prob_smaller(other, price) * prob_equal(ints1_tie, price)
            # if add:
                # print ints1_tie, " | ", other, " : ", "price2", price, "*", add, "=", add * price
            res += add * price
    
    print res