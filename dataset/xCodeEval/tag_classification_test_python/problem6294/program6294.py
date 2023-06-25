def program6294():
    MOD = 998244353
    
    n, k = map(int, input().split())
    x = n - k
    
    num = 1
    den = 1
    s = 0
    #print(x)
    for i in range(x):
    	v = pow(x-i, n, MOD) * num * pow(den, MOD-2, MOD)
    	#print(num, den, (x-i)**n, den, v )
    	s = (s + ((-1)**i) * v) % MOD
    	num = (num * (x-i)) % MOD
    	den = (den * (i+1)) % MOD
    
    num = 1
    den = 1
    for i in range(x):
    	num = (num * (n-i)) % MOD
    	den = (den * (i+1)) % MOD
    #print("=",  s, num, den)
    s = ((1 + (k!=0)) * s * num * pow(den, MOD-2, MOD) % MOD)
    print(s)