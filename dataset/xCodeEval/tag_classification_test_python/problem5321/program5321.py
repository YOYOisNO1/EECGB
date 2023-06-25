def program5321():
    n,m=map(int,input().split())
    dp=[0]*(n+10)
    a=[0]*(n+10)
    dp[n]=1
    a[n]=1
    
    for i in range(n-1,0,-1):
        dp[i]=a[i+1]
        z=2
        while i*z<=n:
            dp[i]+=a[i*z]
            if z*(i+1)<=n:
                dp[i]-=a[z*(i+1)]
            z+=1
            dp[i]%=m
        dp[i]%=m
        a[i]=a[i+1]+dp[i]
        a[i]%=m
    
    print(dp[1])