def program2871():
    import math
    for _ in range(1):
    	n,x,pos=map(int,input().split())
    	fact=[]
    	mod=1000000007
    	fact.append(1)
    	for i in range(n+1):
    		fact.append(((fact[i]%mod)*(i+1)%mod)%mod)
    		#print(fact[i])
    	l=0
    	r=n
    	small,big=x-1,n-x
    	ans=1
    	while l<r:
    		mid=(l+r)//2
    		if mid>pos:
    			r=mid
    			ans*=big
    			ans%=mod
    			big-=1
    		elif mid<=pos:
    			l=mid+1
    			if mid!=pos:
    				ans*=small
    				ans%=mod
    				small-=1
    	ans*=fact[small+big]
    	ans%=mod
    	print(ans%mod)
    
    
    
    