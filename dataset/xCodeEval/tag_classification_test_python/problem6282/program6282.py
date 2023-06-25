    MAX = 2*10**5+100
    MOD = 998244353
    fact = [0]*MAX #fact[i]: i!
    inv = [0]*MAX #inv[i]: iの逆元
    finv = [0]*MAX #finv[i]: i!の逆元
    fact[0] = 1
    fact[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
        
    for i in range(2, MAX):
        fact[i] = fact[i-1]*i%MOD
        inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1]*inv[i]%MOD
    
def C(n, r):
        if n<r:
            return 0
        if n<0 or r<0:
            return 0
        return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD
    
    n, k = map(int, input().split())
    
    if k>=n:
        print(0)
        exit()
        
    if k==0:
        print(fact[n])
        exit()
        
    ans = 0
    
    for i in range(n-k+1):
        if i%2==0:
            ans += C(n-k, i)*pow(n-k-i, n, MOD)
            ans %= MOD
        else:
            ans -= C(n-k, i)*pow(n-k-i, n, MOD)
            ans %= MOD
        
    ans *= 2*C(n, k)
    ans %= MOD
    
    print(ans)