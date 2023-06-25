def program5308():
    n, M = map(int,input().split())
     
    
    
    
    
     
    dp = [0]*(n+1)
    accu = [0]*(n+1)
     
     
    dp[1] = 1
    dp[2] = 2
    extra = 0
    
    
     
    for i in range(3,n+1):
        dp[i] = (2*dp[i-1]) % M
    
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                dp[i] += (dp[j] - dp[j-1] )%M
              
                if j*j<i and j!=1:  
                 
                   dp[i] += (dp[i//j] - dp[i//j-1])%M
                dp[i] = dp[i] % M
    
    
     
    #print(dp)
     
     
     
    print(dp[n])