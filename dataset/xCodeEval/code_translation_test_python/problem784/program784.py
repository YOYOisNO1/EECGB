def program784():
    MOD = pow(10, 9) + 7
    
    n, l, r = map(int, input().strip().split())
    
    a0 = a1 = a2 = 0
    xl = l
    while xl % 3 != 0 and xl < r: xl += 1
    xr = r
    while xr % 3 != 0 and xr > xl: xr -= 1
    
    if xl <= xr and xl % 3 == 0 and xr % 3 == 0: a0 = (xr - xl) // 3 + 1
    
    xl = l
    while xl % 3 != 1 and xl < r: xl += 1
    xr = r
    while xr % 3 != 1 and xr > xl: xr -= 1
    
    if xl <= xr and xl % 3 == 1 and xr % 3 == 1: a1 = (xr - xl) // 3 + 1
    
    xl = l
    while xl % 3 != 2 and xl < r: xl += 1
    xr = r
    while xr % 3 != 2 and xr > xl: xr -= 1
    
    if xl <= xr and xl % 3 == 2 and xr % 3 == 2: a2 = (xr - xl) // 3 + 1
    
    
    dp = [[0 for i in xrange(3)] for j in xrange(n + 1)]
    
    dp[1] = [a0 % MOD, a1 % MOD, a2 % MOD]
    
    for i in xrange(2, n + 1):
        dp[i][0] = dp[i - 1][0] * a0 + dp[i - 1][1] * a2 + dp[i - 1][2] * a1
        if dp[i][0] >= MOD: dp[i][0] %= MOD
        dp[i][1] = dp[i - 1][0] * a1 + dp[i - 1][1] * a0 + dp[i - 1][2] * a2
        if dp[i][1] >= MOD: dp[i][1] %= MOD
        dp[i][2] = dp[i - 1][0] * a2 + dp[i - 1][1] * a1 + dp[i - 1][2] * a0
        if dp[i][2] >= MOD: dp[i][2] %= MOD
    
    print(dp[n][0]) % MOD