def b(a,m): 
        m0=m;y=0;x=1
        if (m==1):return 0
        while (a>1):
            q=a//m;t=m;m=a%m;a=t;t=y;y=x-q*y;x=t
        if (x<0):x=x+m0 
        return x
    p=998244353
    n,m=map(int,input().split())
    z=0
    for i in range(1,n+1): z+=b(i, p)
    print(((1+m*z)*(1+n*b(m+1,p)))%p)