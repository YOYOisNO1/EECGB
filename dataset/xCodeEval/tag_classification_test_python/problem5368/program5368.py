def program5368():
    for i in range(int(input())):
        n,k=map(int,input().split())
        dp=[[1,1] for i in range(k+2)]
        p=pow(2,n-1,int(1e9+7))
        for i in range(1,k+1):
            if n%2:dp[i][1]=(dp[i-1][1]*(p+1))%int(1e9+7)
            else:
                dp[i+1][0]=(dp[i][0]*p*2)%int(1e9+7)
                dp[i][1]=(dp[i-1][1]*(p-1)+dp[i][0])%int(1e9+7)
        print(dp[k][1])
        