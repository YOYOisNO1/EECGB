def program3473():
    n,m=map(int,input().split())
    t=[0]*(m+1)
    for i in range(1,m+1):
        if i<=n%m:
            t[(i*i)%m]+=((n//m)+1)
        else:
            t[(i*i)%m]+=(n//m)
    
    ans=t[0]*t[0]
    for i in range(1,m):
        ans+=t[i]*t[m-i]
    print(ans)