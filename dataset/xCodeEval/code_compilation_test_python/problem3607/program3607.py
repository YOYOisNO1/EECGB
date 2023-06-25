def program3607():
    for u in range(int(input())):
        n, m = map(int, input().split())
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        p = [0]*(n+1)
        cache = [[] for i in range(n+1)]
        
        a = 0
        b = 1
        
        for i in range(2, n+1):
            for j in cache[i]:
                a = (a - dp[p[j]] + m)%m
                p[j] += 1
                a = (a + dp[p[j]])%m
                
            a = (a + dp[1])%m
            dp[i] = (a + b)%m
            b = (b + dp[i])%m
            
            p[i] = 1
            j = 2
            while(i*j <= n):
                cache[i*j].append(i)
                j += 1
                
        print(dp[n])