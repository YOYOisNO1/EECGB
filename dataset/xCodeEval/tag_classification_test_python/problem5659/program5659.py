def program5659():
    from math import inf,floor,ceil
    x,y,n=map(float,input().split())
    m=inf
    ans=""
    for b in range(1,int(n+1)):
        a=floor((x*b)/y)
        z=abs(x/y-a/b)
        if z<m-1e-15:
            m=z
            ans=str(a)+'/'+str(b)
        a=ceil((x*b)/y)
        z=abs(x/y-a/b)
        if z<m-1e-15:
            m=z
            ans=str(a)+'/'+str(b)
    print(ans)