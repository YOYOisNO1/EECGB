def getInts():
        return [int(s) for s in input().split()]
    
def getInt():
        return int(input())
    
def getStrs():
        return [s for s in input().split()]
    
def getStr():
        return input()
    
def listStr():
        return list(input())
    
    M = 10**9+7
    
def solve():
        N, K, D = getInts()
        dp = [[0 for j in range(2)] for i in range(N+1)]
        dp[0][0] = 1
        for i in range(1,N+1):
            for j in range(1,min(K+1,N+1)):
                if j < D:
                    dp[i][0] += dp[i-j][0]
                    dp[i][1] += dp[i-j][1]
                else:
                    dp[i][1] += dp[i-j][0]
                    dp[i][1] += dp[i-j][1]
                dp[i][0] %= M
                dp[i][1] %= M
        return dp[N][1]
        
    ans = solve()
    print(ans)
        
        