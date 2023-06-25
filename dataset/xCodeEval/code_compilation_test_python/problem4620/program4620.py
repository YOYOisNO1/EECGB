    import sys
    range = xrange
    input = input
    import __pypy__
    mulmod = __pypy__.intop.int_mulmod
    
    MOD = 10**9+7
    n, k = [int(x) for x in input().split()]
    
def f(n):
        s = 0
        for i in range(n):
            s += pow(i,k,MOD)
            s %= MOD
        return s
    
    precalc = [0]
    for i in range(k + 1):
        precalc.append((precalc[-1] + pow(i,k,MOD)) % MOD)
    
def interpolate(samples, x):
        x %= MOD
        m = len(samples)
        if x < m:
            return samples[x]
        
        modinv = [1]*m
        for i in range(2, m):
            modinv[i] = mulmod(-(MOD//i), modinv[MOD%i], MOD)
    
        invfac = [1]
        for i in range(1, m):
            invfac.append(mulmod(invfac[-1], modinv[i], MOD))
        invneg_fac = [invfac[i] * (1 - 2 * (i & 1)) for i in range(m)]
    
        base = 1
        for j in range(-x, m - x):
            base = mulmod(base, j, MOD)
        
        s = 0
        for i in range(m):
            pr = precalc[i]
            pr = mulmod(pr, pow(i - x, MOD - 2, MOD), MOD)
            pr = mulmod(pr, mulmod(invneg_fac[i], invfac[m - i - 1], MOD), MOD)
            s = (s + pr) % MOD
        return mulmod(s, base, MOD)
    print (interpolate(precalc, n + 1) - (k == 0)) % MOD