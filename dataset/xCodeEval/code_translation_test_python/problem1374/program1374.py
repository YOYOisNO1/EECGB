def program1374():
    MOD = 998244353
    
    n, m, l, r = map(int, input().split())
    
    if (n*m) % 2 == 1:
    	print(pow(r - l + 1, n * m, MOD))
    else:
    	ans = pow(r - l + 1, n * m, MOD)
    	if (r-l) % 2 == 0:
    		ans += 1
    	ans *= pow(2, MOD-2, MOD)
    	ans %= MOD
    	print(ans)