def program2051():
    MOD = int(1e9+7)
    N = int(1e5+7)
    n,k,d = map(int,input().strip('\n').split(' '))
    dp = [[0,0] for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 0
    for i in range(n+1):
    	for j in range(1,k+1):
    		if i-j<0:
    			continue
    		if j<d:
    			dp[i][0] = (dp[i][0] + dp[i-j][0])%MOD
    			dp[i][1] = (dp[i][1] + dp[i-j][1])%MOD
    		else:
    			dp[i][1] = (dp[i][1] + dp[i-j][0])%MOD
    			dp[i][1] = (dp[i][1] + dp[i-j][1])%MOD
    print(dp[n][1])
    
    