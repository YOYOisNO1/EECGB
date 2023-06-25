def program313():
    n,k=map(int,input().split())
    a=map(int,input().split())
    pos=a.count(1)
    neg=a.count(-1)
    m=0
    for i in range(k):
        s=0;e=0
        for j in range(i,n,k):
            if a[j]==1:
                s+=1
            else:
                e+=1
        m=max(m,abs(pos-s-neg+e))
    print(m)