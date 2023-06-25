def program5422():
    MOD = 1000000007
    
    t = int(input())
    for _ in range(t):
    	n, k = map(int, input().split(' '))
    
    	less = pow(2, n - 1, MOD)
    	equal = (pow(2, n, MOD) - less - 1) % MOD
    	if(n & 1):
    		less = (pow(2, n - 1, MOD) - 1) % MOD
    		equal = (pow(2, n, MOD) - less) % MOD
    
    	ways, ans = 1, pow(pow(2, k, MOD), n, MOD)
    	for b in range(k - 1, -1, -1):
    		x = (less * ways) % MOD
    		x = (x * pow(pow(2, b, MOD), n, MOD)) % MOD
    		ans = (ans - x) % MOD
    		ways = (ways * equal) % MOD;
    
    	print(ans)