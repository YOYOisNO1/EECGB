def solve():
        n, mod = map(int, input().split());m = n*(n-1)//2;dp = [[0]*(n*(n-1)+1) for i in range(n+1)];dp1 = [[0]*(n*(n-1)+1) for i in range(n+1)];dp[1][m] = 1
        for i in range(2, n+1):
            for x in range(m-(i-1)*(i-2)//2, m+(i-1)*(i-2)//2+1):
                for d in range(-i+1, i):dp[i][x+d] = (dp[i][x+d]+dp[i-1][x]*(i-abs(d))) % mod
        for i in range(2, n+1):
            for x in range(m-(i-1)*(i-2)//2, m+(i-1)*(i-2)//2+1):dp1[i][x] = dp1[i-1][x] * i % mod
            for x in range(m-(i-1)*(i-2)//2, m+(i-1)*(i-2)//2+1):
                for d in range(1, i):dp1[i][x-d] = (dp1[i][x-d]+dp[i-1][x]*(i-d)) % mod
        return sum(dp1[-1][m+1:]) % mod
    import sys;input = lambda: sys.stdin.readline().rstrip();print(solve())