def program116():
    import itertools
    
    dp = [[[0 for x in xrange(2)] for x in xrange(110)] for x in xrange(110)]
    mod = 1000000007
    data = map(int, input().split())
    
    n = data[0]
    k = data[1]
    d = data[2]
    dp[0][0][0] = 1
    ans = 0
    for i in range(1, n + 1):
    	for j in range(0, n + 1):
    		for g in range(1, k + 1):
    			if(g > j):
    				break
    			if(g >= d):
    				dp[i][j][1] += dp[i - 1][j - g][0]
    				dp[i][j][1] += dp[i - 1][j - g][1]
    			else:
    				dp[i][j][0] += dp[i - 1][j - g][0]
    				dp[i][j][1] += dp[i - 1][j - g][1]
    
    			dp[i][j][1] %= mod
    			dp[i][j][0] %= mod
    		ans += dp[i][n][1]
    		ans %= mod
    print(ans)