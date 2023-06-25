def program5505():
    n, hh = map(int, input().split())
    
    node_counts = [0]
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for l in range(0, j):
                left = 0
                right = 0
                for h in range(0, i): left += dp[h][l]
                for h in range(0, i-1): right += dp[h][j-l-1]
                dp[i][j] += left * dp[i-1][j-l-1] + dp[i-1][l] * right
    
    s = 0
    
    for i in range(hh, n+1):
        s += dp[i][n]
    
    print(s)