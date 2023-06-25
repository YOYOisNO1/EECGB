def program5296():
    n, mod = map(int, input().split())
    
    dp = [0] * (n + 1)
    dp[n] = 1
    sdp = [0] * (n + 2)
    sdp[n] = 1
    for i in range(n - 1, 0, -1):
        cur = 2
        while True:
            if i * cur > n:
                break
            
            start = i * cur
            end = min(n, (i + 1) * cur - 1)
            
            dp[i] += sdp[start] - sdp[end + 1]
            dp[i] %= mod
            
            cur += 1
        
        dp[i] += sdp[i + 1]
        dp[i] %= mod
        
        sdp[i] = dp[i] + sdp[i + 1]
        sdp[i] %= mod
        
    print(dp[1])