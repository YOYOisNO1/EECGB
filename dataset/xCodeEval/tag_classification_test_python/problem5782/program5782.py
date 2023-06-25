def program5782():
    n=int(input())
    s=input()
    dp=[[0]*(n+1)for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            dp[i][j]=dp[i+1][j]+1
            for k in range(i+1,j+1):
                if s[k]==s[i]:
                    dp[i][j]=min(dp[i][j],dp[i+1][k-1]+dp[k][j])
    print(dp[0][-2])