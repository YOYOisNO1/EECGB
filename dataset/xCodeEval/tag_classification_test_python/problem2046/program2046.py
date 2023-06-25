    import sys
    sys.setrecursionlimit(100000)
    n, k, d = [int(x) for x in sys.stdin.readline().strip().split()]
    memo = {}
    m = 10**9 +7
def dp(n,k,d):
    	key = str(n)+str(d)
    	if n==0:
    		return 1
    	if n<0:
    		return 0
    	if key in memo:
    		return memo[key]
    	s = 0
    	for i in range(1,k+1):
    			if i>=d :
    				s+=dp(n-i,k,0)
    			elif n-i>=d:
    				s+=dp(n-i,k,d)
    	memo[key]=s
    	return s
    print(dp(n,k,d)%m)