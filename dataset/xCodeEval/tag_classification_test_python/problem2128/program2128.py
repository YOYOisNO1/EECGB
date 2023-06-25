def program2128():
    key = 1000000007
    n, k, d = [int(i) for i in input().split()]
    dp = [[0, 0] for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
    	total = 0
    	for j in range(1, min(d, i + 1)):
    		total += (dp[i - j][0] % key)
    	dp[i][0] = total
    for i in range(1, n + 1):
    	total = 0
    	for j in range(1, min(d, i + 1)):
    		total += (dp[i - j][1] % key)
    	for j in range(d, min(i, k) + 1):
    		total += ((dp[i - j][0] + dp[i - j][1]) % key)
    	dp[i][1] = total
    print(dp[n][1]) % key
    