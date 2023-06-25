def program5361():
    MOD = 10 ** 9 + 7
    
    for _ in range(int(input())):
    	n, k = map(int, input().split())
    
    	ans = 1
    	if n%2:
    		ans = pow(1+pow(2,n-1,MOD),k,MOD)
    		print(ans)
    	else:
    		for i in range(1,k+1):
    			ans = pow(pow(2,i-1,MOD),n,MOD) + (pow(2,n-1,MOD)-1)*ans
    			ans %= MOD
    
    		print(ans)