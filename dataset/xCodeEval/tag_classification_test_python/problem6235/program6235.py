def program6235():
    #
    #
    
    cst = 10**9 + 7
    n = int(input(""))
    if n == 0:
    	print(1,)
    
    elif n == 1:
    	print(3,)
    else:		
    	m = pow(2, n - 1, cst)
    	print((m) * (1 + 2*m)) % cst,
    	
    	
    		
    	
    