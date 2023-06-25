def program3922():
    from math import log,ceil
    w,m=map(int,input().split())
    d=[0]*33
    t=int(ceil(log(m+1,w)))
    n=m
    for i in range(t,0,-1):
        p=w**(i-1)
        d[i-1]=n//p
        n=n%p
    f=True
    for i in d:
        if i!=0 and i!=1:
            f=False
            break
    if f:
        print("YES")
        exit(0)
    for i in range(32):
        if d[i]>1:
            d[i]-=w
            d[i+1]+=1
    f=True
    for i in d:
        if i not in range(-1,2):
            f=False
            break
    if f:
        print("YES")
    else:
        print("NO")