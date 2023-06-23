    import sys
    from math import sqrt, floor, factorial, gcd
    from collections import deque, Counter
    inp = sys.stdin.readline
    read = lambda: list(map(int, inp().strip().split()))
    
    
# def getans(n1, n2, k1, k2):
    # 	key = str(n1)+"-"+str(n2)+"-"+str(k1)+"-"+str(k2)
    # 	if key in dp:
    # 		return(dp[key])
    # 	if n1+n2 == 0:
    # 		return(1)
    # 	if n1 > 0 and k1 > 0:
    # 		x = (getans(n1-1, n2, k1-1, l2))
    # 	if n2 > 0 and k2 > 0:
    # 		y = (getans(n1, n2, l_1, k2-1))
    	
    # 	dp[key] = x+y
    # 	return(x+y)
    
def solve():
    	n1, n2, l_1, l_2 = read()
    	dp = dict()
	def getans(n1, n2, k1, k2):
    		key = str(n1)+"-"+str(n2)+"-"+str(k1)+"-"+str(k2)
    		x = 0; y = 0
    		if key in dp:
    			return(dp[key])
    		if n1+n2 == 0:
    			return(1)
    		if n1 > 0 and k1 > 0:
    			x = (getans(n1-1, n2, k1-1, l_2))
    		if n2 > 0 and k2 > 0:
    			y = (getans(n1, n2-1, l_1, k2-1))
    		
    		dp[key] = (x+y)%10**8
    		return((x+y)10**8)
    	print(getans(n1, n2, l_1, l_2))
    
    
    
    
    if __name__ == "__main__":
    	solve()