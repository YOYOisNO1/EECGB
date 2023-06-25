def program1461():
    sok = input().split()
    
    x = int(sok[0]);y = int(sok[1])
    
    d1 = min(x,y)
    
    d2 = (max(x,y))- d1
    
    if d2%2==0:
        print (d1,"",int(d2/2))
    
    else:
        print (d1,"",int(d2/2-0.5)