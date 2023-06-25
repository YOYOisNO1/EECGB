    from functools import lru_cache
    
    MOD = 998244353
    N, X = map(int, input().split())
    
    r = 1
    
    F = [1, 1]
    for i in range(2, N+1):
        F.append((i * F[i-1]) % MOD)
    
    IF = list(F)
    IF[N] = pow(IF[N], MOD-2, MOD)
    for i in range(N-1, 1, -1):
        IF[i] = IF[i+1] * (i+1)
    
def comb(n, k):
        return F[n] * IF[k] % MOD * IF[n-k] % MOD
    
    @lru_cache(maxsize=None)
def g(n, x):
        if n == 1: return 0
        assert x >= 1
    
        dmg = n-1
        if dmg >= x:
            return pow(x, n, MOD)
    
        r = pow(dmg, n, MOD)
        for rem in range(2, n+1):
            #print('cur', n, 'rem', rem, 'x', x)
            attr = (comb(n, rem) * pow(dmg, n-rem, MOD) % MOD * g(rem, x-dmg)) % MOD
            #print(attr)
            r = (r + attr) % MOD
    
        #print(n, x, r)
        return r
    
    
    
    """
    for i in range(2, X+1):
        for j in range(2, N+1):
            print(i, j)
            r = (r + comb(N, j) * pow(i-1, N-j, MOD)) % MOD
    """
    
    print(g(N, X))