def smallestDivisor(n): 
      
        # if divisible by 2 
    	if (n % 2 == 0): 
    		return 2; 
      
        # iterate from 3 to sqrt(n) 
    	i = 3;  
    	while(i * i <= n): 
    		if (n % i == 0): 
    			return i; 
    		i += 2; 
      
    	return n;
    
def pebbles(n,k):
    	k+=n
    	if n==1:
    		return(int(k))
    	else:
    		n=n/smallestDivisor(n)
    		return pebbles(n,k)
    
    
    n=int(input())
    print(pebbles(n,0))