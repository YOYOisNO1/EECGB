def fun(n,k):
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            dp[i]=sum(dp[max(i-k,0):i])
        return dp[n]
    n,k,d=map(int,input().split())
    print((fun(n,k)-fun(n,d-1))%1000000007)