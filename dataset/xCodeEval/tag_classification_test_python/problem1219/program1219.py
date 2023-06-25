    import math
    I=lambda:map(int,input().split())
    a, b, c=I()
    
def simple(l):
        c=0
        for i in range(len(l)):
            c+=int(l[i])
        
        return c
            
    l=[]        
    for i in range(1,82):
        x=pow(i,a)
        y=b*x+c 
        if y>0 and y<=10**9:
           xi=list(str(y))
           xs=simple(xi)
           if xs==i:
              l.append(y) 
    
    print(len(l))
    if len(l)!=0:
       print(*l)               