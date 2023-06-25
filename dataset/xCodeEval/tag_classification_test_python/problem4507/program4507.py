def fact(x,mod):
        f=[1]
        for i in range(1,x+1):
            f.append((f[-1]*i)%mod)
        return f
    n,m=map(int,input().split())
    f=fact(n,m)
    ans=0
    for i in range(1,n+1):
        ans=(ans+(n-i+1)*f[n-i+1]*f[i])%m
    print(ans)