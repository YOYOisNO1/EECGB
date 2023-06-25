def program1990():
    n,k,d=map(int,input().split())
    dp=[[0 for i in range(2)] for i in range(101)]
    dp[0][0]=1
    dp[0][1]=1
    for i in range(1,101):
        
            dp[i][0]=sum(dp[j][0] for j in range(i-min(i,d),i))
            if(min(i,d)==d):
                dp[i][0]=dp[i][0]-dp[i-d][0]
            
                
        
            dp[i][1]=sum(dp[j][1] for j in range(i-min(i,k),i))
                
        
       
            
    pri=10**9+7
    print((dp[n][1]-dp[n][0])%(pri))