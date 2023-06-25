    n = int(input())
    
def prime(n):
    	if n<=3:
    		return True
    	else:
    		for i in range(2,int(n**(0.5))+1):
    			if n % i == 0:
    				return False
    		return True
    
    if prime(n):
    	print(1)
    elif n % 2 == 0:
    	print(2)
    elif prime(n-2):
    	print(2)
    else:
    	print(3)