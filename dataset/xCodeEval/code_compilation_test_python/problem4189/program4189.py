    MOD = 998244353
def inv(x):
        return pow(x, MOD - 2, MOD)
     
    n, m = map(int, input().split())
     
    mult = n * inv(m + 1) + 1
    mult %= MOD
    
    out = m + 1
    for currN in range(1, n):
        out += m * inv(currN)
        out %= MOD
     
    out *= mult
    print(out % MOD)