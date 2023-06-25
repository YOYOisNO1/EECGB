def program2067():
    n, k, d = map(int, input().split())
    
    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for su in range(n + 1):
        for mi in range(k + 1):
            for i in range(1, k + 1):
                if (su + i <= n):
                    dp[su + i][max(i, mi)] += dp[su][mi] % mod
    print((int(sum(dp[n][d:])) % mod))