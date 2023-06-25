    from sys import stdin
    
    
def calculate_main(n, k, mod):
    	dp = [0] *(n + 1)
    	dp[0] = 1; dp[1] = 1
    	for i in range(2, n + 1):
    		for j in range(i - 1, max(- 1, i - k - 1), - 1):
    			dp[i] += dp[j]
    			dp[i] %= mod
    		
    	return dp
    	
    	
    
    # main starts
    n, k, d = list(map(int, stdin.readline().split()))
    mod = 10 ** 9 + 7
    dp = calculate_main(n, k, mod)
    #print(dp)
    dp2 = [0] * (n + 1)
    
    for i in range(d, n + 1):
    	for j in range(1, min(k + 1, i + 1)):
    		if  j < d:
    			dp2[i ] += dp2[i - j]
    			dp2[i ] %= mod
    		else:
    			dp2[i] += dp[i - j]
    			dp2[i] %= mod
    #print(dp2)
    
    print((dp2[n])% mod)