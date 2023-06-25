def program6119():
    a = input() 
    r1 = int(a[0])
    c1 = int(a[2])
    r2= int (a[4])
    c2 = int (a[6])
    if r1 == r2 or c1==c2 : 
        if r1 == r2 and c1==c2 :
           print(0,end=' ')
        else :
           print(1,end=' ')
    else : 
        print(2,end=' ')
    
    if abs(r1-r2) == abs(c1-c2) :
        if r1 == r2 and c1==c2:
           print(0,end=' ')
        else :
            print(1,end=' ')
    elif ( (r1 % 2 ==0 and c1 %2 ==0) or (r1 % 2 !=0 and c1 %2 !=0)) != ((r2 % 2 ==0 and c2 %2 ==0) or (r2 % 2 !=0 and c2 %2 !=0)):
         print(0,end=' ')
    
    else : 
        print(2,end=' ')
    
    
    if abs(r1-r2) >= abs(c1-c2) :
        print(abs(r1-r2))
        
    elif abs(c1-c2) >= abs(r1-r2) :
        print(abs(c1-c2))
    else : 
        print(0)
        