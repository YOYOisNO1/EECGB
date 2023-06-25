def program4984():
    MOD = 1000000007
    
    n, kk = map(int, input().strip().split())
    
    K = kk + 1
    A = 100
    
    dp = [[1 for i in xrange(K)] for j in xrange(A)]
    inv = [pow(i, MOD - 2, MOD) for i in xrange(A + 1)]
    
    ans = 1
    
    p = 2
    while p * p <= n:
        if n % p == 0:
            al = 0
            while n % p == 0: 
                n //= p
                al += 1
            for k in xrange(al + 1): dp[k][0] = p ** k
            for i in xrange(1, al + 1):
                for j in xrange(1, kk + 1):
                    dp[i][j] = 0
                    for k in xrange(i + 1):
                        dp[i][j] += dp[k][j - 1]
                        if dp[i][j] >= MOD: dp[i][j] %= MOD;
                        
                    dp[i][j] = dp[i][j] * inv[i + 1]
                        
                    if dp[i][j] >= MOD: dp[i][j] %= MOD
                
            ans *= dp[al][kk]
                
            if ans >= MOD: ans %= MOD
            
        p += 1
    
    if n > 1: 
        al = 1
        p = n
        for k in xrange(al + 1): dp[k][0] = pow(p, k, MOD)
        for i in xrange(1, al + 1):
            for j in xrange(1, kk + 1):
                dp[i][j] = 0
                for k in xrange(i + 1):
                    dp[i][j] += dp[k][j - 1]
                    if dp[i][j] >= MOD: dp[i][j] %= MOD;
                    
                dp[i][j] = dp[i][j] * inv[i + 1]
                
                if dp[i][j] >= MOD: dp[i][j] %= MOD
            
        ans *= dp[al][kk]
            
        if ans >= MOD: ans %= MOD
        
    print(ans)