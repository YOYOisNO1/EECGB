    mod = 1e9+7
def add(a,b):
    	a += b
    	if a >= mod:
    		return a-mod
    	return a
    
def Sulution():
    	n,k,d = [int(x) for x in input().split()]
    	dp = [[for j in range(100)]0 for i in range(2)]
    	print(dp)
    	dp[0][0] = 1
    	dp[0][1] = 0
    	for i in range(1,n):
    		for j in range(1,k):
    			if i < j:
    				break
    			if j < d:
    				dp[i][0] += dp[i-j][0]
    				dp[i][1] += dp[i-j][1]
    			else:
    				dp[i][1] += dp[i-j][0]
    				dp[i][1] += dp[i-j][1]
    			if dp[i][0] >= mod:
    				dp[i][0] -= mod
    			if dp[i][1] >= mod:
    				dp[i][1] -= mod
    
    	return dp[n][1]
    
    print(Sulution())