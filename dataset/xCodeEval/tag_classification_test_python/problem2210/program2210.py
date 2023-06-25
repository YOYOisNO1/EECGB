def gcd(a,b):
        a,b=min(a,b),max(a,b)
        while a>0:
            a,b=b%a,a
        return b
    a,b,c,d=map(int,input().split())
    t=(a*b//gcd(a,b))
    x=c//t
    y=d//t
    if c%t==0 :
        print(y-x+1)
    else:
        print(y-x)
    
    
    
    
    
    
    
    