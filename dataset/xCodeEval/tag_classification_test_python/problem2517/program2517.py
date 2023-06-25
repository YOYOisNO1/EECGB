def program2517():
    n,k = map(int,input().split())
    MOD = 1000000007 
    
    d = []
    
    for i in range(1,2001):
        cur = []
        for j in range(1,i+1):
            if i%j==0:
                cur.append(j)
        d.append(cur)
    
    dp = []
    
    for i in range(0,k+1):
        cur=[]
        for j in range(0, n+1):
            cur.append(0)
        dp.append(cur)
    
    for i in range(1,n+1):
        dp[1][i] = 1
    
    for i in range(1,k+1):
        for j in range(1,n+1):
            for c in d[j-1]:
                dp[i][j]+=dp[i-1][c]
                if dp[i][j]>=MOD:
                    dp[i][j]-=MOD
    
    ans = 0
    
    for i in range(1,n+1):
        ans+=dp[k][i]
        if ans>=MOD:
            ans-=MOD
    
    print(ans)