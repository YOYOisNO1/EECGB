def program7168():
    import sys
    input = sys.stdin.readline
    
    N,K=map(int,input().split())
    mod=998244353
    
    Combi=[[] for i in range(260)]
    Combi[0]=[1,0]
    
    for i in range(1,260):
        Combi[i].append(1)
        for j in range(i):
            Combi[i].append((Combi[i-1][j]+Combi[i-1][j+1])%mod)
        Combi[i].append(0)
    
    DP=[0]*N
    DP[0]=1
    
    for i in range(K):
        for j in range(N-1,-1,-1):
            x=DP[j]
            for k in range(j+1,N):
                DP[k]+=x*Combi[N-1-j][k-j]%mod*pow(K-i,k*(k-1)//2-j*(j-1)//2,mod)%mod
                DP[k]%=mod
    
    print(DP[-1]%mod)