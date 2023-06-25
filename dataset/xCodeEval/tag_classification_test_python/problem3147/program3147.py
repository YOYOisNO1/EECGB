    import math
def is_prime(n):
        if n % 2 == 0 and n > 2: 
            return False
        elif n==2:
    		return True
        elif n>2:
    		return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    n=int(input())
    
    if is_prime(n):
    	print(1)
    	print(n)
    elif is_prime(n-2):
    	print(2)
    	print('2 ')+str(n-2)
    else:
    	print(3)
    	i=n-8
    	while i>0:
    		i-=1;
    		if is_prime(i):
    			n=n-i
    			print(i,)
    			break	
    	for i in range(n,3,-1):
    		if is_prime(i) and is_prime(n-i):
    			print(i,)
    			print(n-i)
    			break;