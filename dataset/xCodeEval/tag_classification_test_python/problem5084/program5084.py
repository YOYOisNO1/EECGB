def program5084():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    or1=l.count(1)
    or2=n-or1
    dif=0
    for j in range(k):
        i=0
        c1=or1
        c2=or2
        while True:
            c=j+i*k
            if c>=n:
                if dif<abs(c1-c2):
                    dif=abs(c1-c2)
                break
            if l[c]==1:
                c1-=1
            else:
                c2-=1
            i+=1
    print(dif)