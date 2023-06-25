def program1517():
    
    import sys
    input = lambda :sys.stdin.readline()[:-1]
    ni = lambda :int(input())
    na = lambda :list(map(int,input().split()))
    yes = lambda :print("yes");Yes = lambda :print("Yes");YES = lambda : print("YES")
    no = lambda :print("no");No = lambda :print("No");NO = lambda : print("NO")
    #######################################################################
    
    n, m = na()
    dp = [1]*(n+1)
    res = 1
    z = 1
    for i in range(4,n+1,2):
        dp[i] -= 1
    
    for i in range(2,n+1):
        s = (res + dp[i])%m
        for j in range(i*2,n+1,i):
            #print(i, j, s)
            dp[j] += s
            dp[j] %= m
        for j in range((i+1)*2,n+1,i+1):
            #print(i, j, -s)
            dp[j] -= s
            dp[j] %= m
        res = s*2%m
    
    print(s)