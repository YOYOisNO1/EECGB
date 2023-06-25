def program2754():
    import sys
    
    #sys.stdin = open('in.txt', 'r')
    
    n, m, t = map(int, input().split())
    
    dp = [[0] * 31 for _ in xrange(31)]
    for i in xrange(0, 31):
    	for j in xrange(0, i + 1):
    		if i == 0 or j == 0 or i == j:
    			dp[i][j] = 1
    		else:
    			dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    		#print('dp[%d][%d] = [%d]') % (i, j, dp[i][j])
    
    ans = 0
    for i in xrange(4, t):
    	if i <= n and t - i <= m:
    		ans += dp[n][i] * dp[m][min(t - i, m - t + i)]
    print(ans)