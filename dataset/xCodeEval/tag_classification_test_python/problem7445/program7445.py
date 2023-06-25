    import sys
    
    
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())
    
    
    n,mod = MI()
    
    m = n*(n-1)//2
    dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0][1] = 1
    for i in range(1,n):
        for j in range(m+1):
            for k in range(n+1):
                a = dp[i][j][k]
                if not a:
                    continue
                dp[i+1][j+i][i+1] += a
                dp[i+1][j+i][i+1] %= mod
                for l in range(i):
                    dp[i+1][j+i-1-l][k] += a
                    dp[i+1][j+i-1-l][k] %= mod
    
    S_dp = [[[0]*(n+1) for k in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for k in range(n+1):
            a = 0
            for j in range(m+1):
                a += dp[i][j][k]
                a %= mod
                S_dp[i][j][k] = a
    
    SS_dp = [[[0]*(n+1) for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            a = 0
            for k in range(n+1):
                a += S_dp[i][j][k]
                a %= mod
                SS_dp[i][j][k] = a
    
    ANS = [0]*(n+1)
    for i in range(1,n+1):
        ans = i*ANS[i-1] % mod
        for k in range(n+1):
            for j in range(1,m+1):
                if not dp[i][j][k]:
                    continue
                ans += dp[i][j][k]*(SS_dp[i][j-1][-1]-SS_dp[i][j-1][k])
                ans %= mod
        ANS[i] = ans
    
    print(ANS[-1])