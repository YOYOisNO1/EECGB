    from sys import stdin
    import math
    
def line():
    	return stdin.readline().strip()
    
    class Fraction():
	def __init__(self, num, denom):
    		self.num = num
    		self.denom = denom
    	
    	@staticmethod
	def gcd(a, b):
    		if b == 0:
    			return a
    		return Fraction.gcd(b, a % b)
    
	def abs(self):
    		return Fraction(abs(self.num), abs(self.denom))
    	
	def sum(self, f):
    		return Fraction(self.num * f.denom + f.num * self.denom, self.denom * f.denom)
    	
	def to_float(self):
    		return float(self.num) / self.denom
    
	def compare(self, f):
    		left = self.num * f.denom
    		right = f.num * self.denom
    		if left < right:
    			return -1
    		elif left > right:
    			return 1
    		return 0
    
def sumf((a,b), (c,d)):
    	return float(a*d + b*c) / float(b*d)
    
    x, y, n = map(float, line().split())
    dist = Fraction(float('inf'), 1)
    num, den = None, None
    
    B = Fraction(int(x), int(y))
    for b in xrange(1, int(n)+1):
    	a1 = int(math.floor(b * x / y))
    	a2 = int(math.ceil(b * x / y))
    	Ab1 = B.sum(Fraction(-a1, b)).abs()
    	Ab2 = B.sum(Fraction(-a2, b)).abs()
    	if dist.to_float() > Ab1.to_float(): # Ab1.compare(dist) < 0:
    		dist, num, den = Ab1, a1, b
    	if dist.to_float() > Ab2.to_float(): # Ab2.compare(dist) < 0:
    		dist, num, den = Ab2, a2, b
    
    print("{}/{}").format(int(num), int(den))