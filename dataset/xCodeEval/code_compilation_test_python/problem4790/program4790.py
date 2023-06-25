def program4790():
    
    import sys
    input = lambda :sys.stdin.readline()[:-1]
    ni = lambda :int(input())
    na = lambda :list(map(int,input().split()))
    yes = lambda :print("yes");Yes = lambda :print("Yes");YES = lambda : print("YES")
    no = lambda :print("no");No = lambda :print("No");NO = lambda : print("NO")
    #######################################################################
    N, M = na()
    mod = M
    dp = [0]*(N+1)
    dp[1] = 1
    z = 1
    for x in range(2,N+1):
        res, R = 0, x
        while R:
            q = x // R
            L = x // (q + 1)
            
            if q != x:
                res += dp[q] * (R - L)
    
                res %= mod
            R = L
        res += z
        res %= mod
        dp[x] = res
        z += dp[x]
        z %= mod
    print(dp[N])