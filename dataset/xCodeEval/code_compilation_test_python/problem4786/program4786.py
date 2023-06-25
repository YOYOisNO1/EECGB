def program4786():
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    dp = [0] * (n + 2)
    dp[n] = 1
    for i in range(n - 1, 0, -1):
        dpi = dp[i + 1]
        j = 2
        while i * j < n + 2:
            dpi += dp[i * j] - dp[min(n + 1, (i + 1) * j)]
            dpi %= m
            j += 1
        dp[i] = dpi + dp[i + 1]
        dp[i] %= m
    ans = (dp[1] - dp[2]) % m
    print(ans)