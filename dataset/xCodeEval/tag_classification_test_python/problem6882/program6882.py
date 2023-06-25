def program6882():
    n, k = map(int, input().split())
    MOD = 10**9+7
    if k >= n:
        print(pow(2, n, MOD))
        exit()
    
    inv = [1]*(n+1)
    f = [1]*(n+1)
    finv = [1]*(n+1)
    for i in range(2, n+1):
        f[i] = f[i-1]*i % MOD
        inv[i] = MOD-(inv[MOD % i]*(MOD//i) % MOD)
        finv[i] = finv[i-1]*inv[i] % MOD
    
    ans = 0
    for i in range(k+1):
        ans += f[n]*finv[i] % MOD*finv[n-i] % MOD
        ans %= MOD
    print(ans)