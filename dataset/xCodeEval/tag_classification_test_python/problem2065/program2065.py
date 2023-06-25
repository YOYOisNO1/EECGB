def program2065():
    r=lambda:map(int,input().split())
    
    n,k,d=r()
    m=10**9+7
    dp=[[1,0]]+[ [0,0] for i in range(n+1) ]
    
    for i in range(1,n+1):
        #print("n "), i
        for j in range(1,k+1):
            #print("j "), j
            if i >= j:
                if j >= d:
                    dp[i][1]+=(dp[i-j][0]+dp[i-j][1])%m
                else:
                    dp[i][0]+=(dp[i-j][0])%m
                    dp[i][1]+=(dp[i-j][1])%m
            #print(dp[i])     
    
    print(dp[n][1]%m)