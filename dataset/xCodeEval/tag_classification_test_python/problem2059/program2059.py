def main():
        n, k, d = map(int, input().split())
        mod = 10 ** 9 + 7
        dp = [[0] * 201, [0] * 201]
        dp[0][0] = 1
        ans = 0
        for i in xrange(n):
            ndp = [[0] * 201, [0] * 201]
            for j in xrange(1, d):
                for l in xrange(n):
                    for b in [0, 1]:
                        ndp[b][l+j] += dp[b][l]
                        if ndp[b][l+j] >= mod:
                            ndp[b][l+j] -= mod
            for j in xrange(d, k+1):
                for l in xrange(n):
                    ndp[1][l+j] += dp[0][l] + dp[1][l]
                    if ndp[1][l+j] >= mod:
                        ndp[1][l+j] -= mod
                    if ndp[1][l+j] >= mod:
                        ndp[1][l+j] -= mod
            dp = ndp
            ans += dp[1][n]
            if ans >= mod:
                ans -= mod
        print(ans)
    main()            