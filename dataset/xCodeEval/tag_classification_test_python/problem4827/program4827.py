def program4827():
    dp=[[[[0 for i in range(11)] for j in range(11)]for k in range(102)] for l in range(102)]
    h,f,k1,k2=map(int,input().split())
    for i in range(h+1):
        for j in range(f+1):
            for k in range(k1+1):
                for l in range(k2+1):
    
                    if i+j==0:
                        ans=1
                    else:
                        ans=0
                        if i>0 and k>0:
                            ans+=dp[i-1][j][k-1][k2]
                        if j>0 and l>0:
                            ans+=dp[i][j-1][k1][l-1]
                    dp[i][j][k][l]=ans%10**8
    print(dp[h][f][k1][k2])