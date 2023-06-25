def program3169():
    w,m,k=map(int,input().split())
    w=w/k
    if w<=0:
        print ans
        exit()
    l=len(str(m))
    s=10**l
    n=l
    w-=n*(s-m)
    ans=s-m
    if w<=0:
        print ans
        exit()
    s*=10
    n+=1
    while w>s:
        ans+=9*s
        w-=9*s*n
        s*=10
        n+=1
    print ans+w/n