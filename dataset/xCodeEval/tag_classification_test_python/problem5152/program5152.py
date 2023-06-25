    N, L, R = map(int, input().split())
    
    # (1s, digits)
    if N == 0:
    	print(0)
    	exit(0)
    dp = [0, 0]
    dp[0] = (0, 1)
    dp[1] = (1, 1)
def solve(n):
    	if n < 2: 
    		dp[n] = (n, 1)
    		return (n, 1)
    	A = solve(n/2)
    	dp.append((A[0]*2 + n%2, A[1]*2 + 1)) 
    	return (A[0]*2 + n%2, A[1]*2 + 1)
    
    solve(N)
    # print(dp)
    
def rem(key):
    	n = len(dp) - 1
    	m = N
    	cost = 0
    	while n >= 0:
    		if key == dp[n][1]: 
    			cost += dp[n][0] 
    			break
    		elif key > dp[n][1]/2:
    			cost += dp[n-1][0] + (m%2)
    			key = dp[n][1]/2 - (dp[n][1] - key)
    			m/=2
    			n-=1
    		else:
    			m/=2
    			n-=1
    	return cost
    
    # print(dp[-1][1]) - R
    print(dp[-1][0]) - rem(L - 1) - rem(dp[-1][1] - R)
    
    
    
    
    
    
    