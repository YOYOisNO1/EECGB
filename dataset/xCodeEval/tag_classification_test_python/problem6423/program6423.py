def program6423():
    import sys
    input = sys.stdin.readline
    
    n,m=map(int,input().split())
    
    DP=[0]*(n+5)
    CUM=[1]*(n+5)
    CUM[1]=0
    DP[1]=1
    
    S=1
    
    for i in range(2,n+1):
        CUM[i]=(CUM[i-1]+CUM[i])%m
        DP[i]=(S+CUM[i])%m
        S+=DP[i]
        S%=m
    
        for j in range(i+i,n+1,i):
            CUM[j]=(CUM[j]+DP[i]-DP[i-1])%m
    
    print(DP[n])
        
        