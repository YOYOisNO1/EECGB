    import sys
    range = xrange
    input = input
    import __pypy__
    mulmod = __pypy__.intop.int_mulmod
    
    MOD = 10**9+7
    n, k = [int(x) for x in input().split()]
    k += 2
    
def f(n):
        s = 0
        for i in range(n):
            s += pow(i,k-2,MOD)
            s %= MOD
        return s
    
    precalc = [0]
    for i in range(k - 1):
        precalc.append((precalc[-1] + pow(i,k-2,MOD)) % MOD)
    
    big = 10**6 + 10
    modinv = [1]*big
    for i in range(2,big):
        modinv[i] = mulmod(-(MOD//i), modinv[MOD%i], MOD)
    
    invfac = [1]
    for i in range(1,big):
        invfac.append(invfac[-1]*modinv[i]%MOD)
    invneg_fac = [invfac[i] * (1 - 2 * (i & 1)) for i in range(len(invfac))]
    
def g(x):
        if x < k:
            return precalc[x]
        base = 1
        for j in range(-x, k - x):
            base = mulmod(base, j, MOD)
        s = 0
        for i in range(k):
            pr = precalc[i]
            pr = mulmod(pr, pow(i - x, MOD - 2, MOD), MOD)
            pr = mulmod(pr, mulmod(invneg_fac[i], invfac[k - i - 1], MOD), MOD)
            s = (s + pr) % MOD
        return mulmod(s, base, MOD)
    
    print((g(n) + 1) - (k == 2)) % MOD