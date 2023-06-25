def program5317():
    
    import sys
    input=sys.stdin.readline #文字列入力はするな！！
    
    n,m=map(int,input().split())
    mod=m
    dp=[0]*(n+3)
    dp[n]=1
    sdp=[0]*(n+3)
    sdp[n]=1
    
    for x in range(n-1,0,-1):
        dp[x]+=sdp[x+1]
        dp[x]%=mod
        z=2
        while x*z<=n:
            l=x*z
            r=(x+1)*z-1
            if r>n:r=n
            dp[x]+=sdp[l]-sdp[r+1]
            dp[x]%=mod
            z+=1
        sdp[x]=sdp[x+1]+dp[x]
        sdp[x]%=mod
    
    print(dp[1]%mod)
    
    
    
    