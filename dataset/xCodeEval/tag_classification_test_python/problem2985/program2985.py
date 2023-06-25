def program2985():
    M = 998244353
    n,m,k = map(int,input().split())
    dp = [[0 for i in range(2005)] for j in range(2005)]
    dp[1][0] = m
    for i in range(1,n):
        for j in range(k+1):
            dp[i+1][j]+=dp[i][j]
            dp[i+1][j]%=M
            dp[i+1][j+1]+=dp[i][j]*(m-1)
            dp[i+1][j+1]%=M
    print(dp[n][k])