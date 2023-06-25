    n,m=map(int,input().split())
    mod=998244353
    if n<=2 or m<=2:
    	print(0)
    elif m-n+1<0:
    	print(0)
    else:
	def pow(n,p):
    		if p==0:
    			return 1
    		a=pow(n,p//2)%mod
    		b=a
    		if p%2==1:
    			b=b*n
    		b%=mod
    		return (a*b)%mod
    	fact = [1 for i in range(200010)]
    	for i in range(1,200002):
    		fact[i]=fact[i-1]*i
    		fact[i]%=mod
    	#print(fact[0:10])
	def inverseModulo(n):
    		a=pow(n,mod-2)%mod
    		return a
    	ans=fact[m];
    	ans*=(n-2);
    	ans%=mod;
    	ans=ans*inverseModulo(fact[n-1]);
    	ans%=mod;
    	ans*=inverseModulo(fact[m-n+1]);
    	ans%=mod;
    	ans*=pow(2,n-3);
    	ans%=mod;
    	print(ans);