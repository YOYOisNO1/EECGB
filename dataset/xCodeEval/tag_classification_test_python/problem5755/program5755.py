    from sys import stdin
    import math
    
def line():
    	return stdin.readline().strip()
    
    x, y, n = map(float, line().split())
    num, den = None, None
    dist = float('inf')
    
    for b in xrange(1, int(n)+1):
    	a1 = math.floor(b * x / y)
    	a2 = math.ceil(b * x / y)
    	Ab1 = abs(a1/b - x/y)
    	Ab2 = abs(a2/b - x/y)
    	if dist - Ab1 > 1e-15:
    		dist, num, den = Ab1, a1, b
    	if dist - Ab2 > 1e-15:
    		dist, num, den = Ab2, a2, b
    
    print("{}/{}").format(int(num), int(den))