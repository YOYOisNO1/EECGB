    	'''input
    	3 6
    	'''
    	from sys import exit
	def primes(n,p):
    		if n%2 == 0:
    			return False
    		d = 2
    		while d*d <= n:
    			while (n % d) == 0:
    				n = n//d
    				if d < p:
    					return False
    			d += 1
    		return True
    
    	p,n = map(int,input().split())
    	for i in range(n,p,-1):
    		if primes(i,p):
    			print i
    			exit(0)
    	print "-1"