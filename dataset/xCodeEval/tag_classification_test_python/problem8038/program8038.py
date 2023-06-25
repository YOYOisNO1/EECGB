    import sys
    range = xrange
    input = input
    
    
def fast_modder(MOD):
        """ Returns function modmul(a,b) that quickly calculates a * b % MOD, assuming 0 <= a,b < MOD """
        import sys, platform
        impl = platform.python_implementation()
        maxs = sys.maxsize
        if 'PyPy' in impl and MOD <= maxs and MOD ** 2 > maxs:
            import __pypy__
            intsub = __pypy__.intop.int_sub
            intmul = __pypy__.intop.int_mul
            intmulmod = __pypy__.intop.int_mulmod
            if MOD < 2**30:
                MODINV = 1.0 / MOD
            def modmul(a, b):
                    x = intsub(intmul(a,b), intmul(MOD, int(MODINV * a * b)))
                    return x - MOD if x >= MOD else (x if x >= 0 else x + MOD)
            else:
            def modmul(a, b):
                    return intmulmod(a, b, MOD)
        else:
        def modmul(a, b):
                return a * b % MOD
        return modmul
    
    
    """ Precalculate factorial, modular inverse of factorial and modular inverse """
    MOD = 998244353
    n, m = map(int, input().split())
    maxN = 2* 10 ** 6 + 10
    modmul = fast_modder(MOD)
    
def mod_precalc():
        """ Calculates fac, inv_fac and mod_inv for i < maxN in O(maxN) time """
        assert maxN <= MOD
        
        fac = [1] * maxN
        for i in range(2, maxN):
            fac[i] = modmul(fac[i - 1], i)
    
        inv_fac = [pow(fac[-1], MOD - 2, MOD)] * maxN
        for i in reversed(range(1, maxN)):
            inv_fac[i - 1] = modmul(inv_fac[i], i)
    
        inv_mod = [modmul(fac[i - 1], inv_fac[i]) for i in range(maxN)]
    
        return fac, inv_fac, inv_mod
    
    fac, inv_fac, inv_mod = mod_precalc()
    
    """ Useful functions involving modulo """
    
def redu(x):
        return x if x < MOD else x - MOD
    
    mult = modmul(n, inv_mod[m + 1]) + 1 
    currN = 1
    out = m + 1
    
    while currN < n:
        currN += 1
        out = redu(out + modmul(m, inv_mod[currN]))
    print(modmul(out, mult))
    