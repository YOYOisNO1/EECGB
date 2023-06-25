def aux(x, a, b, i, vis):
    	stack = [i]
    	while stack:
    		i = stack.pop()
    		if i-b >= 0 and i-b not in vis:
    			vis.add(i-b)
    			stack.append(i-b)
    		if i+a <= x and i+a not in vis:
    			vis.add(i+a)
    			stack.append(i+a)
    
    
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
    
def gcd(a, b):
    	while b > 0:
    		a, b = b, a%b 
    	return a
    
def solve_good(m, a, b):
    	g = gcd(a, b)
    	first = min(m, a+b)
    	vis = set([0])
    	tot = 0
    	for i in xrange(first+1):
    		ct = single(i, a, b, vis)
    		tot += ct
    	tot += g * (sum_seq((m-first)/g + ct) - sum_seq(ct))
    	if (m-first) / g > 0:
    		tot -= ((m-first)/g + ct) * ((g-1) - (m-first) % g)
    	tot += ct * min(g-1, m-first)
    	return tot 
    
    
    
    m, a, b = map(int, input().split())
    print(solve_good(m,) a, b)