def main():
    	a,b,n = map(int,input().split())
    	f,res,mod = [1]*(n+1),0,10**9+7;mod2 = mod-2
    	for i in xrange(1,n+1): 
    		f[i] = f[i-1]*i
    		f[i] %= mod 
    	for i in xrange(n+1):
    		sum = a*i+b*(n-i)
    		check = 1
    		while sum:
    			digit = sum%10
    			if digit != a and digit != b:
    				check = 0
    				break
    			sum /= 10
    
    		res += pow(f[i]*f[n-i],mod2,mod) if check else 0
    	print((res%mod) * f[n]%mod)%mod
    main()