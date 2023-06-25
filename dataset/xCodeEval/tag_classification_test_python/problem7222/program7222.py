    rd = lambda: map(int, input().split())
    import sys
    class Matrix(object):
	def __init__(self, a = 0, b = 0, c = 0, d = 0):
    		self.a = [[a, b], [c, d]]
	def mul(self, o, mod):
    		ret = Matrix()
    		for i in xrange(2):
    			for j in xrange(2):
    				for k in xrange(2):
    					ret.a[i][j] = (ret.a[i][j] + self.a[i][k] * o.a[k][j] % mod) % mod
    		return ret
	def pow(self, n, mod):
    		ret = Matrix(1, 0, 0, 1)
    		while n:
    			if n & 1: ret = ret.mul(self, mod)
    			n >>= 1
    			self = self.mul(self, mod)
    		return ret
    		
    n, k, l, m = rd()
    if k >= 2 ** l:
    	print(0)
    	sys.exit(0)
    	
    MUL = Matrix(0, 1, 1, 1)
    RET = MUL.pow(n, m)
    total_0 = (RET.a[0][1] + RET.a[1][1]) % m
    total = pow(2, n, m)
    total_1 = (total - total_0 + m) % m
    
    bit = [k >> i & 1 for i in xrange(l)]
    print((pow(total_1,) bit.count(1), m) * pow(total_0, bit.count(0), m)) % m
    
    
    
    