def program2055():
    # maa chudaaye duniya
    n, k, d = map(int, input().split())
    dp = [[0 for i in range(3)] for j in range(101)]
    dp[0][0], dp[0][1] = 1, 0
    md = 10**9+7
    for i in range(1, n+1):
        dp[i][0] = dp[i][1] = 0
        for j in range(1, k+1):
            if i<j:
                break
            if j<d:
                dp[i][0] = (dp[i][0] + dp[i-j][0]) % md
                dp[i][1] = (dp[i][1] + dp[i-j][1]) % md
            else:
                dp[i][1] = (dp[i][1] + dp[i-j][0]) % md
                dp[i][1] = (dp[i][1] + dp[i-j][1]) % md
    print(dp[n][1])