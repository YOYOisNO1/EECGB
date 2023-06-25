def program880():
    a=int(input())
    
    b=int(input())
    c=int(input())
    
    d=int(input())
    
    e=int(input())
    f=int(input())
    
    
    big=max(e,f)
    x=min(b,c)
    
    if (big==f):
        if((d-x)>0):
            sum=min(x,d)*f + min(a,(d-x))*e
        else:
            sum=d*f
    else:
        if((d-a)>0)
            sum=min(a,d)*e + min(x,(d-a))*f
        else:
            sum=d*e
    print(sum)