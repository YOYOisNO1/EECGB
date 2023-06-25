    f=[1 for j in range(500055)]
    gf=[1 for j in range(500055)]
    mod=998244353
    for i in range(1,500050):
        f[i]=((f[i-1]*i)%mod)
        gf[i]=(pow(f[i],mod-2,mod))
     
def bc(n,p):
        j=f[n]*gf[p]
        j%=mod;j*=gf[n-p];j%=mod
        return j
    
    n,k=map(int,input().split())
    ans=0
    for j in range(1,n+1):
        p=(n/j)
        if p<k:
            break 
        
        ans=(ans+bc(p-1,k-1))%mod
    print(ans)