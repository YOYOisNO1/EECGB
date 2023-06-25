def program7781():
    #!/usr/bin/python
    
    MOD = 10**9+7
    n = int(input().strip())
    a = map(int, input().split())
    
    c = [[0 for j in xrange(101)] for i in xrange(101)]
    c[0][0] = 1;
    for i in xrange(1, 101):
    	c[i][i] = c[i][0] = 1
    	for j in xrange(1, i+1):
    		c[i][j] = c[i-1][j-1] + c[i-1][j];
    		c[i][j]%=MOD
    
    dp = [[0 for j in xrange(10)] for i in xrange(n+1)]
    for i in xrange(a[9], n+1):
    	dp[i][9] = 1
    
    for d in xrange(8,0,-1):
    	for i in xrange(a[d], n+1):
    		for j in xrange(a[d], i+1):
    			dp[i][d]+=dp[i-j][d+1]*c[i][j]
    			dp[i][d]%=MOD
    
    for i in xrange(a[0]+1, n+1):
    	for j in xrange(a[0], i):
    		dp[i][0]+=dp[i-j][1]*c[i-1][j]
    		dp[i][0]%=MOD
    
    ret = 0
    for i in xrange(1, n+1):
    	ret+=dp[i][0]
    	ret%=MOD
    print(ret)