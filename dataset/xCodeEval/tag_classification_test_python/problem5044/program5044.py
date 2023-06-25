    #!/usr/bin/env python3
    # created : 2020. 8. 18. 00:50
    
    import os
    from sys import stdin, stdout
    
    
def solve(tc):
        w, b = map(int, stdin.readline().split())
    
        dp = [[1.0 for j in range(1001)] for i in range(1001)]
        for i in range(1, 1001):
            dp[i][0] = 1.0
            dp[i][1] = i/(i+1)
            dp[0][i] = 0.0
        dp[1][1] = 0.5
    
        if w == 0:
            print(0.0)
            return
    
        if b == 0:
            print(1.0)
            return
        elif b == 1:
            print(dp[w][b])
            return
    
        for i in range(1, w+1):
            dp[i][2] = i/(i+2)
            dp[i][2] += 2/(i+2) * 1/(i+1)
    
            for j in range(3, b+1):
                dp[i][j] = i/(i+j)
                dp[i][j] += j/(i+j) * (j-1)/(i+j-1) * (j-2)/(i+j-2) * dp[i][j-3]
                dp[i][j] += j/(i+j) * (j-1)/(i+j-1) * i/(i+j-2) * dp[i-1][j-2]
        
        print(dp[w][b])
    
    
    tcs = 1
    tc = 1
    while tc <= tcs:
        solve(tc)
        tc += 1