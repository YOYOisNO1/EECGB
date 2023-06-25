    from sys import stdin
    import math
    
    MOD = 10**9 + 7
    
def line():
    	return stdin.readline().strip()
    
    R = [1, 0, 18, 0, 1800, 0, 670320, 0, 734832000, 0, 890786230, 0, 695720788, 0, 150347555, 0]
    
def dpFun(idx, mask, sum):
    	if mask == done:
    		return 1
    	if (mask, sum) in dp:
    		return dp[mask, sum]
    	c = 0
    	for i in xrange(1, n+1):
    		if mask & (1 << i) == 0:
    			s = (idx + i - 2) % n + 1
    			if sum & (1 << s) == 0:
    				c += dpFun(idx + 1, mask | (1 << i), sum | (1 << s))
    	dp[mask, sum] = c % MOD
    	return dp[mask, sum]
    
    n = int(line())
    done = ((1 << n) - 1) << 1
    dp = {}
    #(dpFun(1, 0, 0) * math.factorial(n)) % MOD
    print(R[n-1])