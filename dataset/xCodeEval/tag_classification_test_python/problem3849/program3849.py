def program3849():
    n = int(input())
    
    dp = [[0, -1, -1] for _ in range(0, n+1)]
    
    l = [int(x) for x in input().split()]
    
    sum = 0
    
    for i in range(0, n):
        cur = l[i]
        
        dp[i+1][0] = dp[i][0] + 1
        
        if dp[i][1] != -1:
            dp[i+1][0] = min(dp[i+1][0], dp[i][1] + 1)
            
        if dp[i][2] != -1:
            dp[i+1][0] = min(dp[i+1][0], dp[i][2] + 1)
        
        if cur == 1 or cur == 3:
            dp[i+1][1] = dp[i][0]
            if dp[i][2] != -1:
                dp[i+1][1] = min(dp[i+1][1], dp[i][2])
        else:
            dp[i+1][1] = -1
        if cur == 2 or cur == 3:
            dp[i+1][2] = dp[i][0];
            if dp[i][1] != -1:
                dp[i+1][2] = min(dp[i+1][2], dp[i][1])
        else:
            dp[i+1][2] = -1
            
    sum = dp[n][0]
    if dp[n][1] != -1:
        sum = min(sum, dp[n][1])
    if dp[n][2] != -1:
        sum = min(sum, dp[n][2])
        
    print(sum)