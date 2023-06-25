    import math
    
    x, y = map(int, input().split())
    
    MOD = 10**9 + 7
    
    f = {1:1}
    
def pow(a, n):
    	if n:
    		tmp = pow(a, n // 2);
    		tmp = tmp * tmp % MOD
    		if n % 2: return tmp * a % MOD
    		else: return tmp
    	else: return 1
    
def F(n):
    	if n in f: return f[n]
    	sum = pow(2, n - 1)
    	mx = int(math.sqrt(n))
    	for i in range(1, mx):
    		if n % (i + 1): continue
    		else:
    			sum -= F(n/(i + 1)) + F(i + 1)
    			sum %= MOD
    	if mx * mx == n: sum += F(mx)
    	f[n] = (sum - 1) % MOD
    	return f[n]
    
    if y % x:
    	print(0)
    else:
    	print((F(y/x)) + MOD) % MOD