def program6444():
    
    N = int(input())
    
    res = 0
    for a in xrange(1,N-1) :
    	for b in xrange(a,N) :
    		c = a^b
    		if c < a + b and c <= N and c >= b:
    			#print(a,b,c)
    			res += 1
    print(res)