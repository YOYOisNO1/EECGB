def g(v):
    	return 0 if v < 0 else v * v
    
def h(v):
    	return 0 if v < 0 else v * (v + 1) / 2
    
def f(v):
    	return g(v + 1) + g(v) - g(v + 1 - x) - g(v + 1 - n - 1 + x) - g(v + 1 - y) - g(v + 1 - n - 1 + y) + h(v + 1 - x - y) + h(v + 1 - n - 1 + x - y) + h(v + 1 - x - n - 1 + y) + h(v + 1 - n - 1 + x - n - 1 + y)
    
    n, x, y, c = map(int, input().split())
    l = 0
    r = c
    while l <= r:
    	v = (l + r) / 2
    	if f(v) < c:
    		l = v + 1
    	else:
    		r = v - 1
    		p = v
    print p