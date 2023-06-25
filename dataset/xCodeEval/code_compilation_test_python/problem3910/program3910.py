def program3910():
    n = int(input())
    dp = [[[0, 0] for x in range(n+1)] for i in range(n+1)]
    mod = 10**9+7
    for i in range(1, n + 1):
        dp[0][i][0] = dp[0][i - 1][1]
        dp[0][i][1] = dp[0][i - 1][0] + 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            t = [0, 0]
            if i > 0:
                dp[i][j][0] += dp[i-1][j][1]
                t[0] = dp[i - 1][j][1]
                t[1] = dp[i - 1][j][0] + 1
            if j > i:
                dp[i][j][0] += dp[i][j-1][1]
                t[0] += dp[i][j - 1][0] + 1
                t[1] += dp[i][j - 1][1]
            for k in t: dp[i][j][1] = max(dp[i][j][1], k)
    print(dp[n][n][1]%mod)