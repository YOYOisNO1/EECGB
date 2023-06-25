def program1991():
    n, k, d = map(int, input().split())
    dp = [[0 for i in range(2)] for j in range(n+1)]
    dp[0][0] = 1
    for v in range(1, n+1):
    	for step in range(1, min(v, k)+1):
    		dp[v][0] += dp[v-step][0]
    		if step >= d:
    			dp[v][1] += dp[v-step][0]
    		else:
    			dp[v][1] += dp[v-step][1]
    print(dp[n][1]) % 1000000007