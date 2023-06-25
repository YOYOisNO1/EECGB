def program882():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    f=int(input())
    x=0
    
    if e>f:
        if a>d:
            return d*e
        elif d>a:
            y=d-a
            x+=a*e
            z=min(y,b,c)
            x+=z*f
    elif f>e:
        if b>d or c>d:
            return d*f
        else:
            y=min(b,c)
            z=d-y
            x+=y*f
            m=min(z,a)
            x+=m*e
            
    return x