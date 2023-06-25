def isPrime(num):
    	for i in xrange(2,int(num**0.5)+1):
    		if num%i==0:
    			return 0
    	return 1
    n=input()
    for i in xrange(n,0,-1):
    	if isPrime(i):
    		if i==n:
    			print 1
    			print i
    		elif isPrime(n-i):
    			print 2
    			print i, n-i
    		else:
    			for j in xrange(2,(n-1),1):
    				if isPrime(j) and isPrime(n-i-j):
    					print 3
    					print i, j, n-i-j
    					break
    		break