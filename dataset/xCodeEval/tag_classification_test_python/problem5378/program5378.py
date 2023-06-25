    import sys
    input = sys.stdin.readline
    
    MAX = 2*10**5+100
    MOD = 10**9+7
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
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
        dp = [[0]*2 for _ in range(k+1)]
        dp[0][0] = 1
        coef00 = 0
        
        for i in range(0, n, 2):
            coef00 += C(n, i)
            coef00 %= MOD
        
        coef01 = 0
        
        for i in range(1, n, 2):
            coef01 += C(n, i)
            coef01 %= MOD
            
        coef10 = 1 if n%2==0 else 0
        coef11 = 1 if n%2==1 else 0
        
        for i in range(k):
            #00
            dp[i+1][0] += dp[i][0]*coef00%MOD
            dp[i+1][0] %= MOD
            dp[i+1][1] += dp[i][1]*coef00%MOD
            dp[i+1][1] %= MOD
            #01
            dp[i+1][1] += dp[i][1]*coef01%MOD
            dp[i+1][1] %= MOD
            #10
            dp[i+1][1] += dp[i][0]*coef10
            dp[i+1][1] %= MOD
            dp[i+1][1] += dp[i][1]*coef10
            dp[i+1][1] %= MOD
            #11
            dp[i+1][0] += dp[i][0]*coef11
            dp[i+1][0] %= MOD
            dp[i+1][1] += dp[i][1]*coef11
            dp[i+1][1] %= MOD
        
        print(sum(dp[k])%MOD)