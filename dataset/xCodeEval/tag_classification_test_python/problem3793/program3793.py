def program3793():
    #  =========     /\       /|    |====/|
    #      |        /  \       |    |   / |
    #      |       /____\      |    |  /  |
    #      |      /      \     |    | /   |
    #  ========= /        \  =====  |/====|  
    #  code
    
    if __name__ == "__main__":
        n,l,r = map(int,input().split())
        dp = [[0,0,0] for i in range(n)]
        MOD = int(1e9 + 7)
    
        t0 = r//3 - (l - 1)//3
        t1 = (r - 1)//3 - (l + 1)//3 + 1
        t2 = r - l - t0 - t1 + 1
    
        dp[0][0] = t0%MOD
        dp[0][1] = t1%MOD
        dp[0][2] = t2%MOD
    
        i = 1
        while i < n:
            dp[i][0] = (dp[i-1][0] * t0 + dp[i-1][1] * t2 + dp[i-1][2] * t1)%MOD
            dp[i][1] = (dp[i-1][0] * t1 + dp[i-1][1] * t0 + dp[i-1][2] * t2)%MOD
            dp[i][2] = (dp[i-1][0] * t2 + dp[i-1][1] * t1 + dp[i-1][2] * t0)%MOD
            i += 1
        print(dp[n-1][0]%MOD)
    
    