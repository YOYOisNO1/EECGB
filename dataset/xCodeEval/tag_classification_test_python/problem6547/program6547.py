def program6547():
    # Catalan interpretation
    
    MOD = 10 ** 9 + 7
    
    n = input() + 1
    dp = [[0 for i in xrange(n)] for j in xrange(n)]
    
    ans = 0
    for i in xrange(n):
        for j in xrange(1):
            dp[i][j] = 1
            if (i + j) & 1: ans += dp[i][j]
    
    for i in xrange(1, n):
        for j in xrange(1, i + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            if dp[i][j] >= MOD: dp[i][j] -= MOD
            if (i + j) & 1: ans += dp[i][j]
            if ans >= MOD: ans -= MOD
    
    print(ans) % MOD