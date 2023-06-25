def program704():
    from fractions import gcd
    a,b,x,y=map(int,input().split())
    g=gcd(x,y)
    x,y=x/g,y/g
    m=min(a/x,b/y)
    print(x*m,y*m)
    