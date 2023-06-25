def program4248():
    a,b,c,d=map(int,input().split())
    dp=[0]*(b+c+2)
    su=0
    for i in range(a,b+1):
        sl=b+i
        sh=c+i
        dp[sl]+=1
        dp[sh+1]-=1
    for i in range(1,b+c+2):
        dp[i]=dp[i]+dp[i-1]
    for i in range(len(dp)-3,-1,-1):
        dp[i]=dp[i+1]+dp[i]
    for i in range(c,d+1):
        if(i<len(dp)-1):
            su+=dp[i+1]
    print(su)
    
        
        
        