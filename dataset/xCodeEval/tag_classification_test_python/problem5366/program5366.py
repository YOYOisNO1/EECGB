    #!/usr/bin/env python3
    # from typing import *
    
    import sys
    import io
    import math
    import collections
    import decimal
    import itertools
    import bisect
    import heapq
    
    
def input():
        return sys.stdin.readline()[:-1]
    
    
    # sys.setrecursionlimit(1000000)
    
    # _INPUT = """3
    # 4 2
    # 2 1
    # 4 0
    # """
    # sys.stdin = io.StringIO(_INPUT)
    
    INF = 10**10
    
    MOD = 1000000007
    
def solve(N, K):
        if K == 0:
            return 1
    
        D = 0
        for i in range(0, N, 2):
            D = (D + comb(N, i)) % MOD
    
        if N % 2 == 1:
            ans = pow(D+1, K, MOD)
            return ans
    
        else:
            D_inv = pow(D, -1+(MOD-1), MOD) #pow(D, -1, MOD)
            n_any = pow(2, N, MOD)
            v = pow(D, K, MOD)
            ans = v
            v = (v * D_inv) % MOD
            ans = (ans + v) % MOD
            for _ in range(K-1):
                v = (v * D_inv * n_any) % MOD
                ans = (ans + v) % MOD
            return ans
    
    fact = [1, 1]  # fact[n] = (n! mod p)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0, 1]  # factinv 計算用
    
def comb(n, r):
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r]) % MOD
    
    N_MAX = 2*(10**5)
    for i in range(2, N_MAX + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)
    
    T0 = int(input())
    for _ in range(T0):
        N, K = map(int, input().split())
        print(solve(N, K))