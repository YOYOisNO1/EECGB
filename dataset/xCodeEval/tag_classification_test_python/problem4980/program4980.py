def program4980():
    MOD = 1000000007
    
    n, kk = map(int, input().strip().split())
    
    K = kk + 1
    A = 1
    
    divi = []
    N = n
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            isprime = 1
            for p in divi:
                if i % p == 0:
                    isprime = 0
                    break
            if isprime:
                ctr = 0
                while n % i == 0: 
                    n //= i
                    ctr += 1
                divi.append(i)
                A = max(A, ctr)
        i += 1
    
    if n > 1: divi.append(n)
    
    A += 1
    
    dp = [[1 for i in xrange(K)] for j in xrange(A)]
    
    ans = 1
        
    for p in divi:
        al = 0
        while N % p == 0:
            N //= p
            al += 1
        
        for k in xrange(al + 1): dp[k][0] = pow(p, k, MOD)
        for i in xrange(1, al + 1):
            for j in xrange(1, kk + 1):
                dp[i][j] = 0
                for k in xrange(i + 1):
                    dp[i][j] += dp[k][j - 1]
                    if dp[i][j] >= MOD: dp[i][j] %= MOD;
                    
                dp[i][j] = dp[i][j] * pow(i + 1, MOD - 2, MOD)
                
                if dp[i][j] >= MOD: dp[i][j] %= MOD
        
        ans *= dp[al][kk]
        
        if ans >= MOD: ans %= MOD
        
    print(ans)