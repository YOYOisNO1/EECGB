def program2515():
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    for i in range(k + 1):
        if i > 0:
            dp[i] = [0] * (n + 1)
        else:
            dp[i] = [1] * (n + 1)
    for i in range(1, k + 1):
        for x in range(1, n + 1):
            for j in range(x, n + 1, x):
                dp[i][x] += dp[i - 1][j]
                dp[i][x] %= 1000000007
    print(dp[k][1])