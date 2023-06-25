    '''input
    5 15
    5 5 5 5 5
    
    '''
    
    RI = lambda : [int(x) for x in input().split()]
    rw = lambda : input().strip()
    
    
    n,k=RI()
    A=RI()
    su = sum(A)
    A= sorted(A,reverse=True)
    Su=[0]*(n+1)
    for i in range(n):
    	Su[i+1]=Su[i]+A[i]
    
    nn = n
    
def canfinish(days):
    	mx = 0
    	for n in range(0,nn+1):
    		su = Su[n]
    		if n == days:
    			mx = su
    
    		addall = n/days - 1
    		addall = (addall + 1)*addall/2
    
    		rem = (n/days )*(n%days)
    		
    		mx = max(mx, su - addall*days - rem)
    		#print(mx,n,addall,days)
    	#print(mid,mx,)
    	return mx
    
    lo = 1
    #print(canfinish(2))
    hi = nn
    ans = 99999999999999
    while lo<=hi:
    	mid = (lo+hi)/2
    	#print(canfinish(mid),mid)
    	if canfinish(mid)>=k:
    		ans = min(ans,mid)
    		hi = mid - 1
    	else:
    		lo = mid + 1
    if ans > n:
    	print(-1)
    else:
    
    	print(ans)
    
    
    
    