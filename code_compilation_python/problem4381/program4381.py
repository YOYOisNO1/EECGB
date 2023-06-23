def program4381():
    n=input()
    #l=[0,1]*((n/2)+1)
    l=[0,1,0,1]
    dp=[[0,0] for i in range(n)]
    dp[0][l[0]]=1
    for i in range(1,n):
        j=i%2
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]
        dp[i][l[j]]+=dp[i-1][int(not l[j])]+1
    print sum(dp[-1])%1000000007