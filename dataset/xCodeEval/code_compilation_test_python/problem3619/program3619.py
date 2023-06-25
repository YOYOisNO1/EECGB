    import io , sys , atexit , os
    
def freopen(filename, mode):
        if mode == "r":
            sys.stdin = open(filename, mode)
    
        elif mode == "w":
            sys.stdout = open(filename, mode)
    
    # ---- MAIN ----
    
    freopen("input.txt", "r")
    #freopen("output.txt", "w")
    
    c = 0
    n,m = map(int,input().split()) 
    
    for i in range(1,m+1):
    	for j in range(1,m+1):
    		num = i*i + j*j 
    		num = num%m 
    		if(num==0): 
    			c += (1+(n-i)/m) * (1+(n-j)/m)
    
    print c
    
    
    
    
    
        
    	
    
    
    
    
    
    
    
    
    
    