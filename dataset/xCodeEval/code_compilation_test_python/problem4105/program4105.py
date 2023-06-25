    n = int(input())
    s = input()
    global p, q, ans
    p = [[0 for i in range(n+1)] for j in range(n+1)]
    q = [[0 for i in range(n+1)] for j in range(n+1)]
    
def f(a, b):
    	global p, q
    	if p[a][b] != 0:
    		return p[a][b]
    	if a > 0:
    		y = f(a-1, b) + (10**(a-1))*int(s[n*2-a-b])
    		if p[a][b] <= y:
    			p[a][b] = y
    			q[a][b] = 'M'
    	if b > 0:
    		y = f(a, b-1) + (10**(b-1))*int(s[n*2-a-b])
    		if p[a][b] <= y:
    			p[a][b] = y
    			q[a][b] = 'H'
    	return p[a][b]
def g(a, b):
    	global q, ans
    	if q[a][b] != 0:
    		ans += q[a][b]
    	if q[a][b] == 'M':
    		g(a-1, b)
    	if q[a][b] == 'H':
    		g(a, b-1)
    
    ans = ''
    f(n, n)
    g(n, n)
    print ans