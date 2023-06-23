    import math
    n,k=tuple(map(int,input().split()))
    dp=[0 for i in range(5*(10**5)+1)]
    x=0
    dp[0]=1
    p=998244353 
    for i in range(1,5*(10**5)+1):
        dp[i]=(i*dp[i-1])%p
def binpow(x,y):
        z=1
        while y>0:
            if y%2==1:
                z=(z*x)%p
            x=(x*x)%p
            y=y//2
        return z
def inversion(x):
        return binpow(x,p-2)
    if(n==k or k==1):
        print(1)
    else:
    for i in range(1,n):
        if(k*i<=n):
            c=n//i
            x+=(dp[c-1]*inversion((dp[k-1]*dp[c-k])%p))%p
        else:
            break
    if(n==k ):
        print(1)
    else:
        print(x%p)