def program517():
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
    
    s = read_str()
    
    res = set()
    for i in xrange(0, len(s) + 1):
        for c in ascii_lowercase:
            t = s[:i] + c + s[i:]
            res.add(t)
    # print(res)
    print(len(res))