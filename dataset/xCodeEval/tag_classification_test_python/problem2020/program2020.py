    mod = 1e9+7
    
def Sulution():
    	n,k,d = [int(x) for x in input().split()]
    	dp = [[0 for i in range(2)]for j in range(101)]
    	dp[0][0] = 1
    	dp[0][1] = 0
    	for i in range(1,n+1):
    		for j in range(1,k+1):
    			if i < j:
    				break
    			if j < d:
    				dp[i][0] += dp[i-j][0]
    				dp[i][0] %= mod
    				dp[i][1] += dp[i-j][1]
    				dp[i][1] %= mod
    			else:
    				dp[i][1] += dp[i-j][0]
    				dp[i][1] %= mod
    				dp[i][1] += dp[i-j][1]
    				dp[i][1] %= mod		
    	return int(dp[n][1])
    
    print(Sulution())