    import sys
    
    factors = []
    
    dp = []
    mod = (int)(1e9+7)
    
    inv_m = 0
    
def sub(a, b):
    	a -= b
    	a %= mod
    	if a < 0: a += mod
    	return a
def add(a, b): return (a + b) % mod
def mul(a, b): return (a * b) % mod
    
def pow(a, b):
    	if b == 0:
    		return 1
    	if b & 1:
    		return mul(a, pow(a, b - 1))
    	else:
    		aux = pow(a, b >> 1)
    		return mul(aux, aux)
    		
def inv(a):
    	return pow(a, mod - 2)
    
def rec(g, m):
    	if g == 1:
    		return 0
    		
    	if dp[g] != -1:
    		return dp[g]
    	
    	fac_len = len(factors[g])
    	X = [0] * fac_len
    	
    	for i in range(fac_len - 1, -1, -1):
    		X[i] = m // factors[g][i]
    		for j in range(i + 1, fac_len):
    			if factors[g][j] % factors[g][i] == 0:
    				X[i] -= X[j]
    				
    	res = 1
    	for i in range(fac_len - 1):
    		prob = mul(X[i], inv_m)
    		cur_res = rec(factors[g][i], m)
    		new_g_res = mul(prob, cur_res)
    		res = add(res, new_g_res)
    	
    	a = mul(m, inv(sub(m, X[-1])))
    	res = mul(res, a)
    	dp[g] = res
    	return res
    
    m = int(sys.stdin.read())
    inv_m = inv(m)
    
    factors = [[] for _ in range(m + 1)]
    for i in range(1, m + 1):
    	j = i
    	while j <= m:
    		factors[j].append(i)
    		j += i
    
    dp = [-1] * (m + 1)
    res = 0
    for i in range(1, m + 1):
    	prob = inv_m
    	cur_res = add(rec(i, m), 1)
    	cur_res = mul(prob, cur_res)
    	res = add(res, cur_res)
    
    print(res)