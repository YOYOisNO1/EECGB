    c = []
    
def f(n, t):
    	x = 0
    	while 2 ** x <= n:
    		x += 1
    	x -= 1
    	ans = c[x][t + 1] if t + 1 <= x else 0
    	if n > 2 ** x and t > 0:
    		ans += f(n - 2 ** x, t - 1)
    		if t == 1:
    			ans += 1
    	return ans
    
    c.append([1])
    for i in range(1, 60):
    	q = [1]
    	for j in range(1, i):
    		q.append(c[-1][j] + c[-1][j - 1])
    	q.append(1)
    	c.append(q)
    
    n, t = map(int, input().split())
    n += 1
    tt = 0
    while t % 2 == 0:
    	t /= 2
    	tt += 1
    if t > 1:
    	print 0
    else:
    	print f(n, tt)