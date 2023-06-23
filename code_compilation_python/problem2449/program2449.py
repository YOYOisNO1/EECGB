    a = int(input())
    
def is_prime(n):
    	for i in range(2,int(n**0.5+1)):
    		if n%i==0:
    			return False
    	else:
    		return True
    		
    if a%2==0 and a>2:
    	    return 2
    	elif is_prime(a):
    	    print 1
    	elif not is_prime(a-2):
    	    print 3