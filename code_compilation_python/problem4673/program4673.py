    dp = {}
def count(n, low):
    	if low == 1: return n
    	k = (n, low)
    	if k in dp: return dp[k]
    	if n < low: return 0
    	l1 = (n-1)/2
    	if l1 < low: return 0
    	l2 = n - 1 - l1
    	dp[k] = 1 + count(l1, low) + count(l2, low)
    	return dp[k]
    
def getPos(l, r, low, want):
    	m = (l+r)/2
    
    	want -= 1
    	if want == 0: return m
    
    	c1 = count(m-l, low)
    	c2 = count(r-m, low+2)
    
    	if c1+c2 >= want:
    		return getPos(l, m-1, low, want-c2)
    	else:
    		return getPos(m+1, r, low, want-c1)
    
    n,k = map(int, input().split())
    if k == 1: print 1
    elif k == 2: print n
    else:
    	lo, hi = 1, n+1
    	while lo < hi:
    		mid = (lo + hi + 1) / 2
    		if count(n, mid) >= k-2:
    			lo = mid
    		else:
    			hi = mid-1
    	print getPos(2,n-1,lo,k-2)