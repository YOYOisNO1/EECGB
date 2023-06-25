    MOD = 998244353
    N = 200007
    fac = [1]*N
    for i in range(1,N):
        fac[i] = (i * fac[i-1])%MOD
    
def inv(n):
        return pow(n,MOD-2,MOD)
    
def nCk(n, k):
        return (fac[n] * inv(fac[k]*fac[n-k] % MOD)) % MOD
    
def nSk(n, k):
        res = 0
        for i in range(1,k+1):
            res = (res + pow(-1,k-i) * nCk(k,i) * pow(i,n,MOD)) % MOD
        return res
    
    n,k = map(int, input().split())
    res = None
    if k == 0:
        res = fac[n]
    elif k >= n:
        res = 0
    else:
        res = (2*nCk(n,k)*nSk(n,n-k))%MOD
    print(res)