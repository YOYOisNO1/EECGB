def program437():
    
    
    a1,a2,a3 = map(int,input().split())
    
    b1,b2,b3 = map(int,input().split())
    
    n = int(input())
    
    suma = a1+a2+a3 
    sumb = b1+b2+b3 
    
    if suma<=5 :
        
        if suma==0 :
            
            shelvesa = 0 
            
        else :
            
            shelvesa = 1
            
    if sumb<=10 :
        
        if sumb==0 :
            
            shelvesb = 0 
            
        else :
            
            shelvesb = 1
            
            
    if suma>5 :
        
        if suma%5 == 0 :
            
            shelvesa = suma//5
            
        else :
            
            shelvesa = suma//5 + 1 
        
    if sumb>10 :
        if sumb%10 ==0 :
            
            shelvesb = sumb//10 
            
        else :
        
            shelvesb = sumb//10 + 1 
        
    #print([shelvesa,shelvesb])
        
    if shelvesa + shelvesb >n :
        
        print("NO")
        
    else :
        
        print("YES")
        
        
        
        
        
        
        
        
        
        