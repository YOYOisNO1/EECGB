def program4311():
    T = int(input())
    n, M = map(int,input().split())
    
    
    dp = [[0 for j in range((n+1)//2)] for i in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][0] =  2**(i-1)
    
    
    
    for i in range(1,n+1):
        for j in range(1,(n+1)//2):
            if j>(i-1)//2: continue 
            dp[i][j] = dp[i-1][j-1]
    
    ans = 0
    for j in range(0,(n+1)//2):
        ans += dp[n][j]
    
    
    
    print(dp)
    print(ans%M)      