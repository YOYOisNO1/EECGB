def program378():
    
    n = int(input())
    
    count = n
    
    i = 1
    
    while n != 0:
    	for ii in range(n - 1):
    		count += i
    
    	i += 1
    	n -= 1
    
    
    print(count)