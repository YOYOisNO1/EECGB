def program4367():
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys, math, random, operator
    from string import ascii_lowercase, ascii_uppercase
    from fractions import Fraction, gcd
    #from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    from Queue import Queue, PriorityQueue
    from collections import deque, defaultdict, Counter
    #getcontext().prec = 100
    
    MOD = 10**9 + 7
    INF = float("+inf")
    
    if sys.subversion[0] == "PyPy":
        import io, atexit
        sys.stdout = io.BytesIO()
        atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
        sys.stdin = io.BytesIO(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip()
    pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
    epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
    die = lambda *args: pr(*args) ^ exit(0)
    
    read_str = input
    read_strs = lambda: input().split()
    read_int = lambda: int(input())
    read_ints = lambda: map(int, input().split())
    read_float = lambda: float(input())
    read_floats = lambda: map(float, input().split())
    
    "---------------------------------------------------------------"
    
    s = read_str()
    
    alpha = ascii_lowercase
    ans = 0
    cur = 0
    for c in s:
        i = alpha.index(c)
        ans += min((i - cur) % 26, (cur - i) % 26)
        cur = i
    print(ans)