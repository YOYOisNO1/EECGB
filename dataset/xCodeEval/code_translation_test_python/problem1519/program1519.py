def solve():
        n, MOD = list(map(int, input().split()))
        dp = [0]*(n+2)
        dp[1] = 1
        dp[2] = -1
        m = 0
        for a in range(1, n+1):
            dp[a] = (dp[a]+2*m%MOD)%MOD
            dp[a+1] = (dp[a+1]-2*m%MOD)%MOD
            m = (m+dp[a])%MOD
            k = 2
            while k*a <= n:
                dp[k*a] = (dp[k*a]+dp[a])%MOD
                c = min(k*a+k, n+1)
                dp[c] = (dp[c]-dp[a])%MOD
                k += 1
        return dp[n]
    
    
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    print(solve())