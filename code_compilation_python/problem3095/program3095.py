def program3095():
    n = input()
    l = len(n)
    pmax = 9**(l-1)
    k = "9"*(l-1)
    if k == "":
        k = 1
    for i in range(int(k),int(n)+1):
        p = 1
        for j in str(i):
            p *= int(j)
        if pmax < p:
            pmax = p
            
    print(pmax)
        
        
            
        
        
        
    
        
        
    
            
            
    
           
            
        
    
                
            
                
                
                
            
                
            
        
        
        
        