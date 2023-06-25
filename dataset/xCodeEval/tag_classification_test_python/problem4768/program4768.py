def program4768():
    import math
    N = 1003
    n = int(input())
    dp = [[1000000000000000000 for i in range(N)] for j in range(62)]
    primes = []
    for i in range(2, 1000):
    	if(len(primes) > 62):
    		break
    	flag = True
    	for j in range(2, i):
    		if(i % j == 0):
    			flag = False
    			break
    	if(flag):
    		primes.append(i)
    
    
    for i in range(1, n + 1):
    	dp[0][i] = min(dp[0][i], 2**(i - 1))
    
    primepowers = [[1 for i in range(n)] for j in range(62)]
    for i in range(1, 62):
    	for j in range(1, n):
    		primepowers[i][j] = primes[i]*primepowers[i][j - 1]
    
    for i in range(1, 62):
    	for j in range(1, n + 1):
    		dp[i][j] = dp[i - 1][j]
    		for k in range(1, int(math.sqrt(j)) + 1):
    			if(j % k != 0):
    				continue
    			dp[i][j] = min(dp[i][j], dp[i - 1][j//k]*primepowers[i][k - 1])
    			dp[i][j] = min(dp[i][j], dp[i - 1][k]*primepowers[i][j//k - 1])
    			
    		# for k in range(0, j + 1):
    		# 	if(j % (k + 1) != 0):
    		# 		continue
    		# 	dp[i][j] = min(dp[i][j], dp[i - 1][j//(k + 1)]*primes[i]**k)
    print(dp[61][n])