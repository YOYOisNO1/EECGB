    MOD = pow(10, 9) + 7
    
    dp1 = [[-1 for i in xrange(102)] for j in xrange(102)]
    dp2 = [-1 for i in xrange(102)]
    
def dp2solve(n, k):
        if dp2[n] != -1: return dp2[n]
        
        if n == 0:
            dp2[n] = 1
            return dp2[n]
            
        if n < 0: return 0
        
        ans = 0
        for i in xrange(1, k + 1): ans += dp2solve(n - i, k)
        ans %= MOD
        dp2[n] = ans
    
        return dp2[n]
    
def dp1solve(n, k, d):
        if dp1[n][d] != -1: return dp1[n][d]
        if n < d: 
            dp1[n][d] = 0
            return dp1[n][d]
        
        ans = 0
        for i in xrange(1, d): ans += dp1solve(n - i, k, d)
        for i in xrange(d, k + 1): ans += dp2solve(n - i, k)
        dp1[n][d] = ans % MOD
            
        return dp1[n][d]
    
    n, k, d = map(int, input().strip().split())
    print(dp1solve(n,) k, d)