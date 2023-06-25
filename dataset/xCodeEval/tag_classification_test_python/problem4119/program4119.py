def program4119():
    n, p, t = map(float, input().split())
    n, t = int(n), int(t)
    dp = [[0 for i in range(t + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
      for j in range(1, t + 1):
        dp[i][j] = p * (dp[i - 1][j - 1] + 1) + (1 - p) * dp[i][j - 1]
    print(dp[n][t])