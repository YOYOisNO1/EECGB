def program7167():
    n,k = map(int,input().split())
    P = 998244353
    C = n + 5
    fact = [1] * C
    fact_inv = [1] * C
    for i in range(2,C):
        fact[i] = fact[i-1] * i % P
    fact_inv[-1] = pow(fact[-1],P-2,P)
    for i in range(C-2,0,-1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % P
    
    
    dp = [[0] * n for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n):
            for u in range(j,n):
                new = u - j
                tmp = new * j + new * (new-1) // 2
                dp[i][u] += dp[i-1][j] * pow(k-i+1,tmp,P) % P * fact_inv[new] % P
        for j in range(n):
            dp[i][j] %= P
    print(dp[-1][-1] * fact[n-1] % P)