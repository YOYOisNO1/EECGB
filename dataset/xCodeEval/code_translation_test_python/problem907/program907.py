def program907():
    a=map(int,input().split())
    b=[0]*3
    d=min(a)
    ans=d
    for i in range(3):
        a[i]-=d
        ans+=a[i]/3
        b[i]=a[i]%3
    if b.count(2)==2 and b.count(0)==1 and d>0:
        ans+=1
    print(ans)