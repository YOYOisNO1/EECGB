def program108():
    n,h,m=map(int,input().split())
    l=[h]*(n+1)
    while m:
        ll,r,x=map(int,input().split())
        for i in range(ll,r+1):
            l[i]=min(x,l[i])
        m-=1
    su=0
    #print(l)
    for i in range(1,n+1):
    
        su+=l[i]**2
    print(su)