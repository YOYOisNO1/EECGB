def program874():
        MOD = 10 ** 9 + 7
        HAVE, NOT_HAVE = 1, 0
         
        n, k, d = map(int, input().split())
         
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        dp[NOT_HAVE][0] = 1
        for dist in range(1, n + 1):
            for weight in range(1, k + 1):
                if weight > dist:
                    break
                if weight >= d:
                    dp[HAVE][dist] += dp[HAVE][dist - weight] + dp[NOT_HAVE][dist - weight]
                    dp[HAVE][dist] %= MOD
                else:
                    dp[NOT_HAVE][dist] += dp[NOT_HAVE][dist - weight]
                    dp[NOT_HAVE][dist] %= MOD
                    dp[HAVE][dist] += dp[HAVE][dist - weight]
                    dp[HAVE][dist] %= MOD
        print(dp[HAVE][n])