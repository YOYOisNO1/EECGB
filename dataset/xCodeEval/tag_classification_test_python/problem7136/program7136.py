    n,k=map(int,input().split())
    dp=[[0 for i in range(0,n)]for j in range(0,k+1)]
    mod = 998244353
def qmi(a,b):
        res=1
        while(b>0):
            if(b%2>0):
                res=res*a%mod
            b>>=1
            a=a*a%mod
        return res
    f=[0 for i in range(500)]
    inv=[0 for i in range(500)]
    f[0]=inv[0]=1
    for i in range(1,500):
        f[i]=f[i-1]*i%mod
        inv[i]=qmi(f[i],mod-2)
def C(a,b):
        if(a<b):
            return 0
        return f[a]*inv[b]*inv[a-b]%mod
    dp[0][0]=1
    # print(k,n,C(5,2),qmi(5,2))
    for i in range(1,k+1):
        for j in range(0,n):
            for kk in range(0,j+1):
                dp[i][j]+=dp[i-1][kk]*C(n-kk-1,j-kk)*qmi(k-i+1,(j-kk)*(j-kk-1)//2 + (j-kk)*kk)  %mod
                dp[i][j]%=mod;
            # print(i,j,dp[i][j])
            # print(i,j,dp[i][j])
    print(dp[k][n-1])