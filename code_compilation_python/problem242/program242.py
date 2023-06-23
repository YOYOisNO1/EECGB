def program242():
    (n, k)=[int(x) for x in input().split()]
    
    res =-1
    dp = [1] * (n+1)
    for i in range(n,0,-1):
        if dp[i] >= k:
            res = i
            break
        imod2 = i % 2
        if imod2 == 0:
            dp[i//2] += dp[i]
        else:            
            dp[i-1] += dp[i]
    
    #print(dp)
    print(res)
    