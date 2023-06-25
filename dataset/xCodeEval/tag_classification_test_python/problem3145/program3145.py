    import math
    
def is_prime(x):
    	if x == 1:
    		return False
    	upto = int(math.sqrt(x))
    	for i in range(2,upto+1):
    		if x%i == 0:
    			return False
    
    	return True
    
    n = int(input())
    if is_prime(n):
    	print("1")
    	print(n)
    else:
    	i = n/2
    	while i > 1:
    		if is_prime(i) and is_prime(n-2*i):
    			print("3")
    			print(i,i,(n-2*i))
    			break
    		i -= 1