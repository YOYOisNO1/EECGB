def program1419():
    n,k=map(int,input().split())
    c=0
    d=2
    l=[]
    while d<=n and c!=k-1:
        if n%d==0:
            n//=d
            c+=1
            l.append(d)
        else:
            d+=1
    if n>1:
        l.append(n)
        print(*l)
    else:
        print(-1)
        