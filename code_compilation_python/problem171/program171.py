def paper():
    	count = 0
    
    	a,b = input("").split()
    	a = int(a)
    	b = int(b)
    
    
    	while a!= b:
    		if a == 1000000000000:
    			return 1000000000000 
    			break
    
    		elif a > b:
    			a = a - b
    			count += 1
    		elif b > a:
    			b = b - a
    			count += 1
    
    	return count + 1
    
    print paper()