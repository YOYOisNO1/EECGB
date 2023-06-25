    #                                               |
    #   _` |  __ \    _` |   __|   _ \   __ \    _` |   _` |
    #  (   |  |   |  (   |  (     (   |  |   |  (   |  (   |
    # \__,_| _|  _| \__,_| \___| \___/  _|  _| \__,_| \__,_|
    
    import sys
    import math
    import operator as op
    from functools import reduce
    
    ## I/O ##
def read_line():
        return sys.stdin.readline()[:-1]
     
def read_int():
        return int(sys.stdin.readline())
        
def read_int_line():
        return [int(v) for v in sys.stdin.readline().split()]
    
def read_float_line():
        return [float(v) for v in sys.stdin.readline().split()]
    ## ##
    
    ## ncr ##
def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer / denom
    ## ##
    
    ## Fenwick Tree ##
    N = int(1e6)+10
    fenwick = [0]*N
    
def add(i,x,n):
    	while i<n:
    		fenwick[i]+=x
    		i = i|(i+1)
    
def fsum(i,n):
    	res = 0
    	while i>=0:
    		res += fenwick[i]
    		i = (i&(i+1))-1
    	return res
    
def fsum_range(i,j,n):
    	return fsum(j,n)-fsum(i-1,n)
    ## ##	
    
    ## Main ##
    
    mod = int(1e9)+7
    
    # t = read_int()
    t = 1
    for i in range(t):
    	n, k, d = read_int_line()
    	dp = [[0,0] for i in range(n+1)]
    	dp[0][0] = 1
    	dp[0][1] = 0
    	for i in range(1,n+1):
    		for j in range(1,min(d-1,i)+1):
    			dp[i][0] += dp[i-j][0]
    		for j in range(1,min(d-1,i)+1):
    			dp[i][1] += dp[i-j][1]
    		for j in range(d,min(k,i)+1):
    			dp[i][1] += (dp[i-j][0]+dp[i-j][1])
    
    	print(dp[n][1]%mod)