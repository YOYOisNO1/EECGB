def program993():
    dp=[[0 for j in range(2001)] for i in range(2001)]
    n,m,k=map(int,input().split())
    for i in range(1,n+1):
        for j in range(k+1):
            if j==0 and i==1:
                dp[i][j]=m
                continue
            if j<=i-1:
                dp[i][j]=(m-1)*dp[i-1][j-1]+dp[i-1][j]
                dp[i][j]%=998244353
    print(dp[n][k])
        
        
        
            
        