def T(n):
    	if n<2:
    		return 1
    	else:
    		return 2*T(n/2)+1
    
def sum_count(n,l,r):
    	val = T(n/2)
    	if n<2:
    		if l<=n<=r:
    			return n%2
    		else:
    			return 0
    	else:
    		if r<= val:
    			return sum_count(n/2,l,r)
    		elif l>val+1:
    			return sum_count(n/2,l-val-1,r-val-1)
    		else:
    			return (n%2)+sum_count(n/2,l,val)+sum_count(n/2,1,r-val-1)
    
    [n,l,r] = input().split()
    n,l,r = int(n),int(l),int(r)
    print(sum_count(n,l,r))