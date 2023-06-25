def otherpl(a, b):
    	k = [1,2,3]
    
    	k.remove(a)
    	k.remove(b)
    
    	return int(k[0])
    
    
    n = int(input())
    
    a = []
    for i in range(n):
    
    	x = int(input())
    	a.append(x)
    
    
    
    
    
    
    
    count = 0
    x = 3
    for i in range(len(a)):
    
    	if a[i] == x:
    		print('NO')
    		break
    
    	
    	else:
    		count += 1	 
    
    
    	x = otherpl(a[i], x)
    	
    if count == len(a):
    	print('YES')		
    
    
    
    