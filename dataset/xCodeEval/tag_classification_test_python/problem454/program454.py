def program454():
    a,b,c,d,e=[int(t) for t in input().split()]
    v=int((a+b+c+d+e)/5)
    t=(a+b+c+d+e)%5
    if t==0 and v!=0:
        print(v)
    elif v==0:
        print(-1)
    else:
        print(-1)