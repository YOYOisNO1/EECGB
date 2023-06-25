    # ---------------------------------------------------Import Libraries---------------------------------------------------
    import sys
    import os
    from math import sqrt, log, log2, log10, gcd, floor, pow, sin, cos, tan, pi, inf, factorial
    from copy import copy, deepcopy
    import bisect
    from sys import exit, stdin, stdout
    from collections import Counter, defaultdict, deque
    from itertools import permutations
    import heapq
    # ---------------------------------------------------Global Variables---------------------------------------------------
    
    # ---------------------------------------------------Helper Functions---------------------------------------------------
    iinp = lambda: int(sys.stdin.readline())
    inp = lambda: sys.stdin.readline().strip()
    strl = lambda: list(inp().strip().split(" "))
    intl =lambda: list(map(int,inp().split(" ")))
    flol = lambda: list(map(float,inp().split(" ")))
    flush  =lambda: stdout.flush()
    
def isPrime(n):
        if n <= 1: return False
        if n <= 3:  return True
        if n%2 == 0 or n%3 == 0: return False
        p=int(sqrt(n))
        for i in range(5,p+1,6):
            if n%i == 0 or n%(i+2) == 0:
                return False
        return True
    
    
    # -------------------------------------------------------Functions------------------------------------------------------
    
def solve():
        n = iinp()
        if n % 2:
            print("NO")
        elif n > 2 and n % 2 == 0:
            print("YES")
        else:
            print("NO")
    
    # -------------------------------------------------------Main Code------------------------------------------------------
    solve()