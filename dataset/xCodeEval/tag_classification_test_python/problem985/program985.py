def program985():
    # Author: S Mahesh Raju
    # Username: maheshraju2020
    # Created on: 30/09/2020 02:34:57
    
    from sys import stdin, stdout, setrecursionlimit
    import heapq
    from math import gcd, ceil, sqrt
    from collections import Counter, deque
    from bisect import bisect_left, bisect_right
    from itertools import combinations, permutations
    ii1 = lambda: int(stdin.readline().strip())
    is1 = lambda: stdin.readline().strip()
    iia = lambda: list(map(int, stdin.readline().strip().split()))
    isa = lambda: stdin.readline().strip().split()
    setrecursionlimit(100000)
    mod = 1000000007
    
    n = ii1()
    a = iia()
    b = iia()
    a2 = max(0, a[0] - (b[0] + b[2])) + max(0, a[1] - (b[1] + b[0])) + max(0, a[2] - (b[2] + b[1]))
    a1 = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    print(a2, a1)