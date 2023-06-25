def isPrime(n):
    	for i in range(2,int(n**(0.5))+1):
    		if (n%i==0):
    			return False
    	return True
    
def minTax(n):
    	if (n==2 or isPrime(n)):
    		print(1)
    		return
    	elif (n%2==0):
    		print(2)
    		return
    	else:
    		if isPrime(n-2):
    			print(2)
    			return
    		else:
    			print(3)
    			return
    
    n = int(input())
    
    minTax(n)