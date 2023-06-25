    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys, math, random, operator
    from string import ascii_lowercase
    from string import ascii_uppercase
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    from Queue import Queue, PriorityQueue
    from collections import deque, defaultdict, Counter
    getcontext().prec = 100
    
    
def lcm(a, b):
        return a * b / gcd(a, b)
    
    
    MOD = 10**9 + 7
    INF = float("+inf")
    
    if sys.subversion[0] != "CPython":  # PyPy?
        input = lambda: sys.stdin.readline().rstrip()
    pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
    
    read_str = input
    read_strs = lambda: input().split()
    read_int = lambda: int(input())
    read_ints = lambda: map(int, input().split())
    read_float = lambda: float(input())
    read_floats = lambda: map(float, input().split())
    
    "---------------------------------------------------------------"
    
    c, h1, h2, w1, w2 = read_ints()
    
    # stage 2
    if w1 < w2:  # most weighted
        (h1, w1), (h2, w2) = (h2, w2), (h1, w1)
    
    mx_h = -1
    n1 = 0
    while w1 * n1 <= c:
        n2 = (c - w1 * n1) / w2
        if n2 >= 0 and n1 * w1 + n2 * w2 <= c:
            add_h = h1 * n1 + h2 * n2
            # print "mxh", n1, n2, ":", add_h
            mx_h = max(mx_h, add_h)
        n1 += 1
    print mx_h