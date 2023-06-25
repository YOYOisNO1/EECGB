def program655():
    
    import math
    
    
    a,b=[int(i) for  i in input().split()]
    
    x=a-b*2
    
    if x<=0:
        print(0,end=" ")
    else:
        print(x, end=" ")
    
    
    if b==0:
        print(a,end=" ")
    else:
        rs = math.ceil((-1 + math.sqrt(1 + 8 * b)) / 2)+1
        x=a-rs
        if x<=0:
            print(0,end=" ")
        else:
            print(x,end=" ")