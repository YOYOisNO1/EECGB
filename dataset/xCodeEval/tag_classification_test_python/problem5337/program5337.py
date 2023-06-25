def program5337():
    n,m=map(int,input().split())
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(2, n+1):
        if i>2: dp[i]=(dp[i]+dp[i-1]+dp[i-1]+1)%m
        for j in range(i+i, n+1, i):
            dp[j]=(dp[j]+dp[i]-dp[i-1])%m
    print((dp[n]+m)%m)