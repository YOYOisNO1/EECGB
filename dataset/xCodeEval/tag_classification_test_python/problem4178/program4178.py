def program4178():
    import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
    
    n=I();dp=[0]*(n+1);s=1
    for i in range(1,n+1):
        for j in range(i*2,n+1,i):dp[j]+=1
    for i in range(1,n+1):dp[i]=(s+dp[i])%mod2;s=(s+dp[i])%mod2
    print(dp[n])