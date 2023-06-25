def program2095():
    n, k, d = map(int, input().split())
    MOD = int(1e9+7)
    dp = [[[0]*(n+1) for i in range(n+1)] for z in range(2)]
    dp[0][0][0] = 1
    res = 0
    for i in range(1,n+1):
    	for s in range(1, n+1):
    		d0 = 0
    		d1 = 0
    		for v in range(1, min(d,s+1)):
    			d0 += dp[0][i-1][s-v]
    			d1 += dp[1][i-1][s-v]
    		for v in range(d, min(k+1,s+1)):
    			d1 += dp[0][i-1][s-v]
    			d1 += dp[1][i-1][s-v]
    		dp[0][i][s] = d0 % MOD
    		dp[1][i][s] = d1 % MOD
    	res += dp[1][i][n]
    print(res % MOD)