    MOD = 998244353
    BIG = 1000000
    fac = [1] * BIG
    for i in range(1, BIG):
        fac[i] = (i*fac[i-1])%MOD
    
def choose(n,k):
       return (fac[n]*pow((fac[k]*fac[n-k])%MOD,MOD-2,MOD))%MOD
    
    n,m = map(int, input().split())
    if n == 2:
        print(0)
    else:
        print((choose(m,n-1) * (n-2) * pow(2,n-3,MOD)) % MOD)