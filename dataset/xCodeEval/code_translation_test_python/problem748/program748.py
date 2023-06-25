def pow3(a, b, mod) :
        ans = 1
        while b > 0 :
            if b & 1 :
                ans = (ans * a) % mod
            a = (a * a) % mod
            b >>= 1
        return ans
    
    class comb :
    	inf = 0
    	fact = []
    	inv = []
    
	def __init__(self, n, infi) :
    		self.fact.extend([0] * (n + 1))
    		self.inv.extend([0] * (n + 1))
    		self.inf = infi
    		self.fact[0] = 1
    		for i in range (1, n + 1) :
    			self.fact[i] = (self.fact[i - 1] * i) % self.inf
    		for i in range (0, n + 1) :
    			self.inv[i] = pow3(self.fact[i], self.inf - 2, self.inf)
    
	def ncr(self, n, r) :
    		ans = self.fact[n]
    		ans = (ans * self.inv[r]) % inf
    		ans = (ans * self.inv[n - r]) % inf
    		return ans
    
	def f(self, n) :
    		return self.fact[n]
    
	def iv(self, n) :
    		return self.ivf[n]
    		
    inf = 998244353
    n, k = list(map(int, input().split()))
    c1 = comb(n, inf)
    ans = 0
    #for i in range (2, n) :
        #print(c1.ncr(i, 2))
        
    i = 1
    while i * k <= n :
        cnt = n // i - 1
        r = k - 1
        ans = (ans + c1.ncr(cnt, r)) % inf
        i += 1
    
    print(ans)