def program5019():
    n,m=map(int,input().split(" "))
    dp=[[[1,0] if j and not i else [0,0] for i in range(m+1)] for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j][0]=(i/(i+j)) + (j/(i+j))*dp[i][j-1][1]
            dp[i][j][1]=(j/(i+j))*(dp[i][j-2][0]*((j-1)/(i+j-1)) + dp[i-1][j-1][0]*((i)/(i+j-1)))
    
    print(dp[n][m][0])