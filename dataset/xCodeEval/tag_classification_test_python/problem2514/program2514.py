def program2514():
    R = lambda: map(int, input().split())
    n, k = R()
    dp = [[0 for j in range(n + 1)] for i in range(k + 1)]
    for l in range(1, n + 1):
        dp[1][l] = 1
    for i in range(1, k):
        for p in range(1, n + 1):
            np = p
            while np <= n:
                dp[i + 1][np] = (dp[i + 1][np] + dp[i][p]) % 1000000007
                np += p
    print(sum(dp[k][p] for p in range(1, n + 1)) % 1000000007)