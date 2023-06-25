def program2125():
    MOD=1000000007
    n,k,d=map(int,input().split())
    dp1=[0]*(n+5)
    dp2=[0]*(n+5)
    dp1[0]=1;dp2[0]=1
    for i in range(1,n+1):
        s=0
        for j in range(1,k+1):
            if j<=i:
                s=(s+dp1[i-j])%MOD
        dp1[i]=s
    for i in range(1,n+1):
        s=0
        for j in range(1,k+1):
            if j<=i:
                if j>=d:
                    s=(s+dp1[i-j])%MOD
                elif i-j>=d:
                    s=(s+dp2[i-j])%MOD
        dp2[i]=s
    print(dp2[n])