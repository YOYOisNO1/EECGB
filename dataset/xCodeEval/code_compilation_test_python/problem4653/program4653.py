def aux(x, a, b, i, vis):
    	if i-b >= 0 and i-b not in vis:
    		vis.add(i-b)
    		aux(x, a, b, i-b, vis)
    	if i+a <= x and i+a not in vis:
    		vis.add(i+a)
    		aux(x, a, b, i+a, vis)
    
    
def single(x, a, b, vis):
    	if x-a in vis:
    		vis.add(x)
    		aux(x, a, b, x, vis)
    	return len(vis)
    
def sum_seq(n):
    	return n * (n+1) / 2
    
def solve(m, a, b):
    	vis = set([0])
    	tot = 0
    	for i in xrange(m+1):
    		one = single(i, a, b, vis)
    		tot += one
    		if i > 0 and one == i + 1:
    			return tot + sum_seq(m+1) - sum_seq(i+1)
    	return tot
    
    
    m, a, b = map(int, input().split())
    print solve(m, a, b)