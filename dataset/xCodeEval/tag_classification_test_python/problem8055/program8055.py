    from fractions import gcd
    n,k = map(int,input().split())
def Q(n):
    	o = n
    	i = 2
    	while i*i<=n:
    		if n%i==0:
    			o = o/i*(i-1)
    			while n%i==0:
    				n = n/i
    		i+=1
    	#print(n,o)
    	if n>1:
    		o = o/n*(n-1)
    	return o
    
    #print(Q(10))
    
    k = (k+1)/2
    while n>1 and k:
    	n = Q(n)
    	k =k-1
    print(n%1000000007)
    