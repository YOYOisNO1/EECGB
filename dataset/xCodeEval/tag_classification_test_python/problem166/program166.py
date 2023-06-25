    # 0 5 0 2 3 - saknar 1, 4
    # UDDA
    
    # U * U --> U ger 0, J ger 2.
    # J * J --> speglat
    # U * J --> spelar ingen roll
    
    # dp[i, j] = antal sätt om du använt j av dina jämna.
    
    # dp[]
    
    N = int(input())
    
    v = [int(x) for x in input().split()]
    
    have = set(v)
    dont_have = set(range(1, N+1)) - have
    
    n_even = len([x for x in dont_have if x % 2 == 0])
    n_odd = len(dont_have) - n_even
    
    # dp[0, 0] = 0 - no swaps yet
    # dp[0, >0] = -inf (or None) - impossible
    # dp[i+1, j+1] = no choice if v[i] is not zero
    
    import functools
    
    INF = 2**20
    
    @functools.lru_cache(maxsize=None)
def rec(idx, even_used, last_even):
        if idx == 0 and even_used == 0: return 0
        if idx == 0: return INF
        if even_used > n_even: return INF
        if even_used < 0: return INF
        i = idx-1
        if v[i] != 0:
            is_even = v[i] % 2 == 0
            if last_even != is_even: return INF
            return min(rec(i, even_used, True) + int(not is_even),
                       rec(i, even_used, False) + int(is_even))
            
        # try all combs of last and this mod 2:
        if last_even:
            return min(rec(i, even_used-1, True),
                       rec(i, even_used-1, False) + 1)
        else:
            return min(rec(i, even_used, True) + 1,
                       rec(i, even_used, False))
    
    #assert(rec(1, 1, True) == 0)
    #assert(rec(1, 1, False) == INF)
    #assert(rec(1, 0, True) == INF)
    #assert(rec(1, 0, False) == 0)
    
    print(min(rec(N, n_even, False), rec(N, n_even, True)))