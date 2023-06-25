def program4717():
    [n,m,k]=[int(i) for i in input().split()]
    [n1,n2]=[int(i) for i in input().split()]
    e1=0
    e2=0
    p1=n1//(m*k)
    if(p1*m*k!=n1):
        p1+=1
    else: e1=m
    p2=n2//(m*k)
    if(p2*m*k!=n2): p2+=1
    else:e2=m
    t=0
    t+=min(min(abs(p2-p1),abs(n+p1-p2)),abs(n+p2-p1))*15
    if (e1==0):
        e1=n1%(m*k)//k
        if(n1%k!=0): e1+=1
    if (e2==0):
        e2=n2%(m*k)//k
        if(n2%k!=0): e2+=1
    if(e1<4):
        t+=(e1-1)*5
    if(e2<4):
        t+=(e2-1)*5
    if(e1>=4):
        t+=10+e1-1
    if (e2 >= 4):
            t += 10 + e2 - 1
    print(t)