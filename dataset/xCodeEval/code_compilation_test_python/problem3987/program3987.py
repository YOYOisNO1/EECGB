    n, a, b, c = [int(i) for i in input().split()]
    set_ = set()
    
def findWays(n, a, b, c):
    	if (n < 0):
    		return 0
    	if (n == 0):
    		t = a*100 + b*10 + c
    		if t not in set_:
    			set_.add(a*100 + b*10 + c)
    			return 1
    	ways = 0
    	if (a > 0):
    		ways += findWays(n - 0.5, a - 1, b, c)
    	if (b > 0):
    		ways += findWays(n - 1, a, b - 1, c)
    	if (c > 0):
    		ways += findWays(n - 2, a, b, c - 1)
    	return ways
    
    print(findWays(n, a, b, c))