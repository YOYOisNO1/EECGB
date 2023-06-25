def program7724():
    n,m,s=map(int,input().split())
    import math
    ans=math.ceil(float(n)/s)*math.ceil(float(m)/s)
    if n%s==0:
        x=s
    else:
        x=n%s
    if m%s==0:
        y=s
    else:
        y=m%s
    #print(ans,x,y)
    ans*=x*y
    print(int(ans))