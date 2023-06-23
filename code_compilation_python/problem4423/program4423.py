def g():
        return map(int,input().split())
    a,b=g()
    c,d=g()
    e,f=g()
    z,r,i=f*f+e*e,0,4
    while i:
        i-=1
        a,b=b,-a
        x,y=c-a,d-b
        r |= (z==0 and x==0 and y==0) | (z and (x*e+y*f)%z==0 and (y*e-x*f)%z==0)
    print("YES") if r else "NO"