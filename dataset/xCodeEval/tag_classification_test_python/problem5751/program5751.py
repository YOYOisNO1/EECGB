    from sys import stdin
    import math
    
def line():
    	return stdin.readline().strip()
    
    class Fraction():
	def __init__(self, num, denom):
    		self.num = num
    		self.denom = denom
    	
	def __repr__(self):
    		return "{}/{}".format(self.num, self.denom)
    	
    	@staticmethod
	def gcd(a, b):
    		if b == 0:
    			return a
    		return Fraction.gcd(b, a % b)
    	
	def reduce(self):
    		g = self.gcd(self.num, self.denom)
    		return Fraction(self.num / g, self.denom / g)
    
	def __abs__(self):
    		return Fraction(abs(self.num), abs(self.denom))
    	
	def __add__(self, f):
    		return Fraction(self.num * f.denom + f.num * self.denom,
    					self.denom * f.denom)
    	
	def __sub__(self, f):
    		return Fraction(self.num * f.denom - f.num * self.denom,
    					self.denom * f.denom)
    	
	def __float__(self):
    		return float(self.num) / self.denom
    
	def __cmp__(self, f):
    		left = self.num * f.denom
    		right = f.num * self.denom
    		if left < right:
    			return -1
    		elif left > right:
    			return 1
    		return 0
    
    x, y, n = map(float, line().split())
    dist = float('inf')
    F = Fraction(float('inf'), 1)
    
    B = Fraction(int(x), int(y))
    for b in xrange(1, int(n)+1):
    	F1 = Fraction(int(math.floor(b * x / y)), b)
    	F2 = Fraction(int(math.ceil(b * x / y)), b)
    	Ab1 = float(abs(B - F1))
    	Ab2 = float(abs(B - F2))
    	if Ab1 < dist:
    		dist, F = Ab1, F1
    	if Ab2 < dist:
    		dist, F = Ab2, F2
    
    print(F)