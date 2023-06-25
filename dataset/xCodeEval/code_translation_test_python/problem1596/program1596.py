def program1596():
    n, M = map(int,input().split())
     
    
    
    
    
     
    dp = [0]*(n+1)
    accu = [0]*(n+1)
     
     
    dp[1] = 1
    dp[2] = 1
    accu[1] = 1
    accu[2] = 2
    extra = 0
    
    
     
    for i in range(3,n+1):
        dp[i] = accu[i-1] 
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                dp[i] += dp[j]
                dp[i] = dp[i] % M
                if j>1 and j*j<i:  
                    dp[i] += dp[i//j]
                    dp[i] = dp[i] % M
        accu[i] = (accu[i-1] + dp[i])%M
    
    
    
     
    #print(dp)
     
     
     
    print(accu[n])