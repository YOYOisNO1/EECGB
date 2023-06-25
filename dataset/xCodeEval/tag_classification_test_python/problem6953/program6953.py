def makediv(n):
    	lower_divisors , upper_divisors = [], []
    	i = 1
    	while i*i <= n:
    		if n % i == 0:
    			lower_divisors.append(i)
    			if i != n // i:
    				upper_divisors.append(n//i)
    		i += 1
    	return lower_divisors + upper_divisors[::-1]
    
    
    from math import gcd
    mod = 10**9 + 7
    n = int(input())
    ans = 0
    for c in range(1, n-1):
    	w = makediv(n-c)
    	wm = len(w)
    	dp = [0] * wm
    	for i in range(wm-1,-1,-1):
    		dp[i] = (n-c) // w[i] - 1
    		for j in range(i+1,wm):
    			if w[j] % w[i] == 0:
    				dp[i] -= dp[j]
    		ans += c * w[i] * dp[i] // gcd(w[i], c)
    		ans %= mod
    
    print(ans)