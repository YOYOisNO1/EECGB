    from sys import stdin
    from fractions import Fraction
    import math
    
def line():
    	return stdin.readline().strip()
    
def sumf((a,b), (c,d)):
    	return float(a*d + b*c) / float(b*d)
    
    x, y, n = map(float, line().split())
    num, den = None, None
    dist = float('inf')
    
    B = Fraction(int(x), int(y))
    for b in xrange(1, int(n)+1):
    	a1 = int(math.floor(b * x / y))
    	a2 = int(math.ceil(b * x / y))
    	Ab1 = abs(sumf((x, y), (-a1, b)))
    	Ab2 = abs(sumf((x, y), (-a2, b)))
    	if dist > Ab1:
    		dist, num, den = Ab1, a1, b
    	if dist > Ab2:
    		dist, num, den = Ab2, a2, b
    
    print("{}/{}").format(int(num), int(den))