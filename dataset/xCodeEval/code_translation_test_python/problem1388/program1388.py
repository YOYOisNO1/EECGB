    from collections import deque, defaultdict, Counter
    from heapq import heappush, heappop, heapify
    from math import inf
    from functools import lru_cache
    from itertools import accumulate
    from typing import List
    import sys
    input = sys.stdin.readline
    
    MOD = 10**9 + 7
    
def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
        max_n = min(max_n, mod - 1)
    
        fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
        fact[0] = 1
        for i in range(max_n):
            fact[i + 1] = fact[i] * (i + 1) % mod
    
        inv_fact[-1] = pow(fact[-1], mod - 2, mod)
        for i in reversed(range(max_n)):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    def nCr_mod(n, r):
            res = 1
            while n or r:
                a, b = n % mod, r % mod
                if a < b:
                    return 0
                res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
                n //= mod
                r //= mod
            return res
    
        return nCr_mod
    
    N, K = map(int, input().split())
    nCr = make_nCr_mod(N, MOD) 
    if K >= N:
        print(2**N % MOD)
    else:
        ans = 1
        for i in range(1, K+1):
            ans += nCr(N, i) % MOD
        print(ans % MOD)