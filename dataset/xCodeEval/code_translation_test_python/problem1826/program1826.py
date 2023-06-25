def main():
        n, k, m = map(int, input().split())
        if k == 1:
            print(9) * pow(10, n - 1, m) % m
            return
        if n == 1:
            print(len([i) for i in xrange(1, 10) if i % k == 0]) % m
            return
        dp = [0] * k
        for i in xrange(10):
            if i % k:
                dp[i%k] += 1
        t = 10 % k
        kk = [[i * j % k for j in xrange(11)] for i in xrange(k)]
        for i in xrange(n - 1):
            ndp = [0] * k
            for j in xrange(1, k):
                for l in xrange(i == n - 2, 10):
                    x = j + kk[t][l]
                    if x >= k:
                        x -= k
                    if x:
                        ndp[x] += dp[j]
                        if ndp[x] >= m:
                            ndp[x] -= m
            for l in xrange(i == n - 2, 10):
                if kk[t][l]:
                    ndp[kk[t][l]] += 1
            dp = ndp[:]
            t = kk[t][10]
        print((9) * pow(10, n - 1, m) - sum(dp) % m + m) % m
    main()