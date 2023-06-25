    import math
    getInputList = lambda : list(input().split())
    getInputIntList = lambda : list(map(int,input().split()))
    
    
    n = int(input())
    
    h = n//2
    left = 1 
    right = n
    
def eat(k,n):
    	a = 0
    	while n > 0:
    		#print(a,n,k)
    		a += min(k,n)
    		n -=  min(k,n)
    		n -=  (n*10)//100
    	return a
    
    ans = eat(39259424579862572,n)
    if n != 1:
    	while left <= right:
    		m = (left + right)//2
    		eat1 = eat(m,n)
    		eat2 = 0
    		if m-1 > 0:
    			eat2 = eat(m-1,n)
    		
    		if eat1 >= h and eat2 < h:s
    			print(m)
    			break
    		if eat1 < h:
    			left = m
    		else:
    			right = m
    		
    else:
    	print(1)