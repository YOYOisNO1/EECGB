def program5643():
    import math
    n,m=map(int,input().split())
    
    if n==1 or m==1:
        print(n*m)
    else:
        if n==2:
            print(m/4*4+min(m%4*2,4))
        else:
            if m==2:
                print(n/4*4+min(n%4*2,4))
            else:
                print(n*m/2+(n*m)%2)
            
    
    
            
            
            
    
    