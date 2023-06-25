def program2007():
    n, k, d = input().split()
    
    n = int(n)
    k = int(k)
    d = int(d)
    
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
    
    for i in range(k + 1):
        dp[i][0] = 1
    
    for j in range(1, n + 1):
        for i in range(1, k + 1):
            dp[i][j] = sum(dp[i][max(0, j - i):j + 1])
    
    print((dp[k][n] - dp[d - 1][n])%(10**9 + 7))