    mo = 10 ** 13
    p = [
    	1, 60, 300, 1500, 15000, 150000, 1500000, 15000000,
    	150000000, 1500000000, 15000000000, 150000000000,
    	1500000000000, 15000000000000
    ]
    
    class mat(object):
	def __init__(self, a, b, c, d):
    		self.a, self.b, self.c, self.d = a, b, c, d
	def times(self, k):
    		return mat(
    			(self.a * k.a + self.b * k.c) % mo,
    		    (self.a * k.b + self.b * k.d) % mo,
    		    (self.c * k.a + self.d * k.c) % mo,
    		    (self.c * k.b + self.d * k.d) % mo
    		)
	def copy(self):
    		return mat(self.a, self.b, self.c, self.d)
    
    me, mt = mat(1, 0, 0, 1), mat(0, 1, 1, 1)
    
def fib(k):
    	ans, t = me.copy(), mt.copy()
    	while k > 0:
    		if k & 1:
    			ans = ans.times(t)
    		t = t.times(t)
    		k >>= 1
    	return ans.b
    
def gene(a, ta, b, tb, tab):
    	ab = []
    	for i in a:
    		for j in b:
    			y = -j // tb - 1
    			while j + y * tb < 0:
    				y += 1
    			while j + y * tb < tab:
    				if (j - i + y * tb) % ta == 0:
    					ab.append(j + y * tb)
    				y += 1
    	return ab
    
def filt(a, f, m):
    	r = f % m
    	return [i for i in a if (fib(i) % m == r)]
    
    if __name__ == '__main__':
    	f = int(input())
    	a = filt(list(range(p[1])), f, 10)
    	b = a[:]
    
    	for i in range(2, 14):
    		m = 10 ** i
    		b = gene(a, p[1], b, p[i - 1], p[i])
    		b = filt(b, f, m)
    
    	print(min(b) if b else -1)