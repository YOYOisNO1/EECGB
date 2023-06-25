def program5088():
    x,y=map(int,input().split())
    p=list(map(int,input().split()))
    l=list()
    i=1
    while i<=y:
        k=i
        su=sum(p)
        for j in range(x):
            if j+1==k:
                su-=p[j]
                k+=y
        l.append(abs(su))
        i+=1
    print(max(l))