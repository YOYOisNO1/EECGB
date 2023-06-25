def program867():
    #Copied
    
    n,m,c,d=map(int,input().split())
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,n+1):
        if(i<c):dp[0][i]=dp[0][i-1]
        else:dp[0][i]=max(dp[0][i-c]+d,dp[0][i-1])
    for i in range(1,m+1):
        a,b,c,d=map(int,input().split())
        for j in range(1,n+1):
            if(j<c):
                dp[i][j]=dp[i-1][j]
            else:
                for k in range(a//b+1):
                    if(k*c<=j):dp[i][j]=max(dp[i][j],dp[i-1][j-k*c]+k*d)
                    else:break
    print(dp[m][n])            