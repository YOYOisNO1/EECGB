def main():
        n = int(input())
        mod = 1000000007
        dp = [[0, 0]]
        for i in xrange(1, n + 1):
            ndp = [[0, 1] for _ in xrange(i + 1)]
            for j in xrange(i + 1):
                if j < i:
                    ndp[j][0] += dp[j][1]
                    ndp[j][1] += dp[j][0]
                    if ndp[j][0] >= mod:
                        ndp[j][0] -= mod
                    if ndp[j][1] >= mod:
                        ndp[j][1] -= mod
                if j > 0:
                    ndp[j][0] += ndp[j-1][1]
                    ndp[j][1] += ndp[j-1][0]
                    if ndp[j][0] >= mod:
                        ndp[j][0] -= mod
                    if ndp[j][1] >= mod:
                        ndp[j][1] -= mod
            dp = ndp
        print(dp[-1][0])
    main()