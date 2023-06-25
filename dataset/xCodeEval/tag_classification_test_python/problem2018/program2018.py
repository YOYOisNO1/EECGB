def program2018():
    t = 10**9 + 7
    
    n, k, d = map(int, input().split())
    
    dp = [[0 for i in range(k + 1)]for i in range(n + 1)]
    
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                break
            if j < d:
                dp[i][0] = ((dp[i][0] % t) + (dp[i - j][0] % t)) % t
                dp[i][1] = ((dp[i][1] % t) + (dp[i - j][1] % t)) % t
            else:
                dp[i][1] = ((dp[i][1] % t) + (dp[i - j][0] % t) + (dp[i - j][1] % t)) % t
    
    print(dp[n][1])