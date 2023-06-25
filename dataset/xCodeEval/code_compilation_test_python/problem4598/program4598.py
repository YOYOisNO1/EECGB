def program4598():
    M = 10 ** 9 + 7
    n, p = map(int, input().split())
    s = [[1, 2, 0]]
    i = j = 0
    x = 3
    while x <= p:
    	a = min(s[i][1] * 3 + 2, p)
    	b = min(s[j][1] * 3 / 2, p)
    	c = min(set(range(0, 3)) - set([s[i][2], s[j][2]]))
    	if a <= b:
    		i += 1
    	if b <= a:
    		j += 1
    	y = min(a, b)
    	if s[-1][2] == c:
    		s[-1][1] = y
    	else:
    		s += [[x, y, c]]
    	x = y + 1
    c = [0] * 3
    for l, r, v in s:
    	c[v] += (2 * p - l - r) * (r - l + 1) / 2
    u = [1, 0, 0, 0]
    for _ in range(n):
    	v = [0] * 4
    	for i, x in enumerate(u):
    		for j, y in enumerate(c):
    			v[i ^ j] = (v[i ^ j] + x * y) % M
    	u = v
    print sum(u[1 : ]) % M