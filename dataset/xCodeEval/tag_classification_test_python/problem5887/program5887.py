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
    
def gcd(a, b):
        """
        Return greatest common divisor using Euclid's Algorithm.
        """
        if a == 0: return b
        if b == 0: return a
        while b:
            a, b = b, a % b
        return abs(a)
    
    
def lcm(a, b):
        """
        Return lowest common multiple.
        """
        if not a or not b:
            raise ZeroDivisionError("lcm arguments may not be zeros")
        return abs(a * b) // gcd(a, b)
    
    "---------------------------------------------------------------"
    
    n = read_int()
    arr = [x - 1 for x in read_ints()]
    if len(set(arr)) != len(arr):
        die(-1)
    
    xs = set(xrange(len(arr)))
    cs = []
    cycle = []
    while xs:
        x = xs.pop()
        cycle.append(x)
        while 1:
            x = arr[x]
            if x == cycle[0]:
                break
            cycle.append(x)
            xs.remove(x)
        cs.append(cycle)
        cycle = []
    
    ans = 1
    for l in map(len, cs):
        cur = l if l & 1 else (l / 2)
        ans = lcm(ans, cur)
    print(ans)