def program552():
    fun=lambda:map(int,input().split())
    n,m=fun()
    data=fun()
    ans=0
    tmp=m
    i=0
    while i < n:
        if data[i]<=tmp:
            tmp-=data[i]
            i+=1
        else:
            tmp=m
            ans+=1
    if tmp != m:
        ans+=1
    print(ans)