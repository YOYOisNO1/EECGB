def program1997():
    n,k,d=map(int,input().strip().split(' '))
    dp=[0]*(n+k+1) 
    vp=[0]*(n+k+1)
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i]+=dp[i-j]  
            if j>=d:
                continue 
            else:
                vp[i]+=vp[i-j]  
        if i<=k:
            dp[i]+=1 
            if i>=d:
                continue 
            else:
                vp[i]+=1  
    print((dp[n]-vp[n])%(10**9 + 7))