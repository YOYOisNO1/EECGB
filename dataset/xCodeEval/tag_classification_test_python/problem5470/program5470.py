def program5470():
    n, h = map(int,input().split())
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    dp[0] = [1 for j in range(n + 1)]
    for i in range(n + 1):
    	for j in range(1, n + 1):
    		for k in range(i):
    			dp[i][j] += dp[k][j - 1] * dp[i - 1 - k][j - 1]
    print(dp[n][n] - (h > 0 and [dp[n][h - 1]] or [0])[0])