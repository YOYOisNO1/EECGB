def program4243():
    
    
    
    x1,y1 = map(int,input().split())
    
    x2,y2= map(int,input().split())
    
    
    
    a = abs(x1-x2)+1
    b = abs(y1-y2)+1
    
    if a==1:
        a+=1
    if b==1:
        b+=1
    print((a+b)*2)