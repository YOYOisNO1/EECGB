def program5442():
    R=lambda:map(int,input().split())
    m,n=R()
    a={}
    for x in R():
        a[x]=a.get(x,0)+1
    a=a.values()
    b=0
    for d in range(1,10001):
        y=m
        for x in a:
            y-=x/d
        if y>0:
            break
        b=d
    print(b)