def program2700():
    R=lambda:map(int,input().split())
    n,m=R()
    a=R()
    b=[]
    s=0
    for i in range(n-1):
        if a[i]%2:
            s+=1
        else:
            s-=1
        if not s:
            b+=abs(a[i+1]-a[i]),
    t=0
    for x in sorted(b):
        if m>=x:
            t+=1
            m-=x
        else:
            break
    print(t)