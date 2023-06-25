    import __pypy__
    modmul = __pypy__.intop.int_mulmod
    
    MOD = 998244353
def inv(x):
        return pow(x, MOD - 2, MOD)
     
    n, m = map(int, input().split())
     
    mult = n * inv(m + 1) + 1
    mult %= MOD
     
    currN = 1
    out = m + 1
    while currN < n:
        currN += 1
     
        out += modmul(m, inv(currN), MOD)
        out %= MOD
     
    out *= mult
    print(out % MOD)