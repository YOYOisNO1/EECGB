def program2038():
    n,k,d = map(int,input().split())
    mod = 1000000007
     
     
    dp = [[0 for j in range(2)] for i in range(n+1)]
     
    dp[0][0] = 1
    dp[0][1] = 0
    
    for i in range(1,n+1):
    	for j in range(1,k+1):
    		if i-j<0: break
    		if j < d:
    			dp[i][0] = (dp[i][0] + dp[i-j][0])%mod
    			dp[i][1] = (dp[i][1] + dp[i-j][1])%mod
    		else:
    			dp[i][1] = (dp[i][1] + dp[i-j][0] + dp[i-j][1])%mod
    
    ans = dp[n][1]%mod
    
    print(ans)