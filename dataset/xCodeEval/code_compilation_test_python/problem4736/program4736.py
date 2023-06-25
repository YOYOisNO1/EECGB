def F(i, n, t):
    	if i + 1 < t:
    		return 0
    	if not t:
    		return 1
    	if n & 2 ** i:
    		return c.get((i, t), 0) + F(i - 1, n ^ 2 ** i, t - 1)
    	else:
    		return F(i - 1, n, t)
    
    d = dict((2 ** i, i) for i in range(50))
    c = {(0, 0) : 1}
    for i in range(1, 50):
    	c[(i, 0)] = c[(i, i)] = 1
    	for j in range(1, i):
    		c[(i, j)] = c[(i - 1, j - 1)] + c[(i - 1, j)]
    n, t = map(int, input().split())
    if t in d:
    	t = d[t] + 1
    	print F(49, n + 1, t) - (t == 1)
    else:
    	print 0