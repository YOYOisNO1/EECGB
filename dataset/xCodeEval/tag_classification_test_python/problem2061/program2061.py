def program2061():
    n,k,d=map(int,input().split())
    dp=[[0 ,0 ] for i in range(n+1)]
    dp[0][0]=1
    dp[0][1]=0
    for i in range(1,n+1):
        dp[i][0]=dp[i][1]=0
        # for q in dp:
        #     print(q)
        # print('-----------')
        for j in range(1,k+1):
            if i-j<0:
                break
            if j<d:
                dp[i][0] += dp[i-j][0]
                dp[i][0]%=1000000007
                dp[i][1] += dp[i - j][1]
                dp[i][1] %= 1000000007
            else:
                dp[i][1]+=dp[i-j][0]
                dp[i][1] %= 1000000007
                dp[i][1]+=dp[i-j][1]
                dp[i][1] %= 1000000007
        #     print(i,j)
        #     for q in dp:
        #         print(q)
        # print('==================')
    print(dp[n][1])