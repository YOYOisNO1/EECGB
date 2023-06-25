def program5732():
    x,y,n=map(int,input().split())
    t=float(x)/float(y)
    r=1e9
    a=b=0
    for i in range(1,n+1):
        w=round(t*float(i))
        tt=w/float(i)
        u=abs(t-tt)
        if r-u>1e-15:
            r=u
            a=w
            b=i
    if abs(t-a/b)==abs(t-(a-1)/b):
        a-=1
    print(str(int(a))+"/"+str(b))