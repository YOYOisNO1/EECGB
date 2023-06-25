def program1442():
    a=input()
    b=int(a[0])
    c=0
    z=0
    for i in range (b):
        x=input()
        for i in x :
            if i in "CMYWGB" :
                c=c+1
    
    
            if i in "WBG" :
                z=z+1
    
    
    
    
    if z>=c:
        print("#Black&White")
    else:
        print("#Color")
    
    
    
    
    
    
    
    
    