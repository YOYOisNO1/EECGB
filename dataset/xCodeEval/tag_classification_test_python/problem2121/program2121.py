def program2121():
    # -*- coding: utf-8 -*-
    """
    Created on Sat Feb  9 00:29:59 2019
    
    @author: Jheel
    """
    
    MOD = 1000000007
    
    n, k, d = map(int, input().split())
    
    dp = [0 for i in range(n+1)]
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        for j in range(max(0,i-k),i):
            dp[i] += dp[j]
            #print(j)
        #print(dp[i])
            
    dp2 = [0 for i in range(n+1)]
    
    dp2[0] = 1
    dp2[1] = 1
    
    for i in range(2,n+1):
        for j in range(max(0,i-d+1),i):
            dp2[i] += dp2[j]
        #print(dp2[i])
    
    ans = dp[n] - dp2[n]
    if n == 1 and d <= 1:
        ans = 1
    
    if ans>MOD:
        ans = ans % MOD
    print(ans)
    