    #
def f(n, k, d):
        dp = [[0, 0] for _ in xrange(n+1)]
        dp[0][0], dp[0][1] = 1, 0
        for i in xrange(1, n+1):
            for j in xrange(1, k+1):
                if j > i:
                    break
                if j < d:
                    dp[i][0] += dp[i-j][0]
                    dp[i][1] += dp[i-j][1]
                else:
                    dp[i][1] += dp[i-j][0] 
                    dp[i][1] += dp[i-j][1]
        return dp[n][1]
    n, k, d = map(int, input().split())
    print(f(n,) k, d)%(10**9+7)