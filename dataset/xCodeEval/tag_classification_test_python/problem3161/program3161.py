def program3161():
    
    
    args = str(input()).split(" ")
    
    n = int(args[0])
    m = int(args[1])
    
    a = n/2 
    if a == m:
    	a += 1
    
    elif m < a: 
    	a = m + 1
    else:
    	a = m - 1
    
    if a == 0:
    	a = 1
    	
    print(a)