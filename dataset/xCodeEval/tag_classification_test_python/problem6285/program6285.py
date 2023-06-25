    f=[1 for j in range(200055)]
    gf=[1 for j in range(200055)]
    mod=998244353
    for i in range(1,200050):
        f[i]=((f[i-1]*i)%mod)
        gf[i]=(pow(f[i],mod-2,mod))
     
def bc(n,p):
        j=f[n]*gf[p]
        j%=mod;j*=gf[n-p];j%=mod
        return j
    n,k=map(int,input().split())
    if n<=k:
        print(0)
    elif k==0:
        print(f[n])
    else:
        ans=0
        for j in range(n-k+1):
            if j%2:
                ans=(ans-pow((n-k-j),n,mod)*bc(n-k,n-k-j))%mod
            else:
                ans=(ans+pow((n-k-j),n,mod)*bc(n-k,n-k-j))%mod
        print((2*ans*bc(n,k))%mod)