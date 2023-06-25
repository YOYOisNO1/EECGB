def borders(p, exclude):
    	l, r, u, d = 0, 0, 0, 0
    	for i in range(len(p)):
    		if i == exclude:
    			continue
    		if p[l][0] > p[i][0]:
    			l = i
    		if p[r][0] < p[i][0]:
    			r = i
    		if p[d][1] > p[i][1]:
    			d = i
    		if p[u][1] < p[i][1]:
    			u = i
    	dx = p[r][0] - p[l][0]
    	dy = p[u][1] - p[d][1]
    	return dx == dy, l, r, d, u
    
def sol(p):
    	good, l, r, d, u = borders(p, -1)
    	if good:
    		for i in range(len(p)):
    			if not (p[i][0] == p[l][0] or p[i][0] == p[r][0] or p[i][1] == p[d][1] or p[i][1] == p[u][1]):
    				return i
    		assert(False)
    	if borders(p, l)[0]:
    		return l 
    	if borders(p, r)[0]:
    		return r 
    	if borders(p, u)[0]:
    		return u
    	assert(borders(p, d)[0]) 
    	return d
    
    n = int(input())
    p = []
    for i in range(4 * n + 1):
    	x, y = map(int, input().split())
    	p.append((x, y))
    ans = sol(p)
    print(*p[ans])