def program7137():
    # import io,os
    # read = io.BytesIO(os.read(0, os.fstat(0).st_size))
    # I = lambda:map(int, read.readline().split())
     
    import sys
    I=lambda:[*map(int,sys.stdin.readline().split())]
    
    n, k = I()
    M = 998244353
    
    facs = [1]
    for i in range(n):
    	facs.append(facs[-1] * (i + 1) % M)
    ifacs = [pow(facs[i], M - 2, M) for i in range(n + 1)]
    
    dp = [[0] * n for i in range(k + 1)]
    for i in range(k + 1):
    	dp[i][0] = 1
    # for i in range(n):
    # 	dp[1][i] = pow(k, i * (i - 1) // 2, M)
    for i in range(1, k + 1):
    	for j in range(1, n):
    		for l in range(0, j + 1):
    			val = dp[i - 1][l]
    			diff = j - l
    			edges = diff * l + diff * (diff - 1) // 2
    			binom = facs[n - 1 - l] * ifacs[diff] * ifacs[n - 1 - l - diff] % M
    			dp[i][j] = (dp[i][j] + val * binom * pow(k + 1 - i, edges, M)) % M
    
    print(dp[-1][-1])
    #print(dp)