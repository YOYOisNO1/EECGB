def power(x,y):
    	mod=1000000007
    	res = 1
    	while (y > 0):
    	// If y is odd, multiply x with result
    		if (y and 1):
    			res = (res * x)%mod
    		y = y >> 1 
    		x = (x * x)%mod
    	return res
    x,k=map(int,input().split())
    mod=1000000007
    x%=mod
    factor=power(2,k)
    factor%=mod
    ans=((2*factor*x)%mod- (factor)%mod+1)%mod
    if x==0:
    	print("0")
    else:
    	print(ans)