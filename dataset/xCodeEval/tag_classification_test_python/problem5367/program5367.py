    try:
        import sys
        from functools import lru_cache, cmp_to_key
        from heapq import merge, heapify, heappop, heappush
        # from math import *
        from collections import defaultdict as dd, deque, Counter as C
        from itertools import combinations as comb, permutations as perm
        from bisect import bisect_left as bl, bisect_right as br, bisect, insort
        from time import perf_counter
        from fractions import Fraction
        import copy
        from copy import deepcopy
        import time
        starttime = time.time()
        mod = int(pow(10, 9) + 7)
        mod2 = 998244353
    
    def data(): return sys.stdin.readline().strip()
    def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
    def L(): return list(sp())
    def sl(): return list(ssp())
    def sp(): return map(int, data().split())
    def ssp(): return map(str, data().split())
    def l1d(n, val=0): return [val for i in range(n)]
    def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
    
        # sys.setrecursionlimit(int(pow(10,6)))
        # from sys import stdin
        # input = stdin.buffer.readline
        # I = lambda : list(map(int,input().split()))
        # import sys
        # input=sys.stdin.readline
    
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    except:
        pass
    
    
    MOD = 10 ** 9 + 7
    
    for _ in range(L()[0]):
        n, k = L()
    
        ans = 1
        if n%2:
            ans = pow(1+pow(2,n-1,MOD),k,MOD)
            print(ans)
        else:
            for i in range(1,k+1):
                ans = pow(pow(2,i-1,MOD),n,MOD) + (pow(2,n-1,MOD)-1)*ans
                ans %= MOD
    
            print(ans)