def program2262():
    n,k = I()
    a,b = I()
    
    if 0:
    	print(1,n*k)
    else:
    	i=abs(a-b);j=a+b;mi,ma=10**9,0
    	while i<=n*k:
    		st = (n*k)//gcd(i,n*k)
    		ma=max(ma,st);mi = min(mi,st)
    		i+=k
    		st = (n*k)//gcd(j,n*k)
    		ma=max(ma,st);mi = min(mi,st)
    		j+=k
    	print(mi,ma)