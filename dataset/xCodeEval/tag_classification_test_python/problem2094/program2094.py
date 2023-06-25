    import sys
    from functools import lru_cache, cmp_to_key
    from heapq import merge, heapify, heappop, heappush
    from math import *
    from collections import defaultdict as dd, deque, Counter as C
    from itertools import combinations as comb, permutations as perm
    from bisect import bisect_left as bl, bisect_right as br, bisect
    from time import perf_counter
    from fractions import Fraction
    sys.setrecursionlimit(int(pow(10,6)))
    # sys.stdin = open("input.txt", "r")
    # sys.stdout = open("output.txt", "w")
    mod = int(pow(10, 9) + 7)
    mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
    # @lru_cache(None)
    
    n,k,d=l()
    dp1=[0 for i in range(n+1)]
    dp2=[0 for i in range(n+1)]
    dp1[0]=1
    dp2[0]=1
    K=[i for i in range(1,k+1)]
    D=[i for i in range(1,d)]
    
    for i in range(n):
        for c in K:
            if(i+c>=n+1):
                break
            dp1[i+c]+=dp1[i]
    
    for i in range(n):
        for c in D:
            if(i+c>=n+1):
                break
            dp2[i+c]+=dp2[i]
    # print(*dp1)
    # print(*dp2)
    print((dp1[-1]-dp2[-1])%mod)