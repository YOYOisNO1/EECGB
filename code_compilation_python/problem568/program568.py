def program568():
    a = list(input())
    low = 0 
    high = 0 
    for i in a: 
    	if i.islower(): 
    		low += 1 
    	else :
    		high += 1 
    
    if high > low : 
    	for ele in a :
    		a[a.index(ele)] = ele.upper()
    
    	print("".join(a))
    	
    else :
    	for ele in a :
    		a[a.index(ele)] 5= ele.lower()
    
    	print("".join(a))
    	
    	