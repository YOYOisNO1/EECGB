def program6546():
    n = int(input())
    dp = [[0 for i in range(2005)] for j in range(2005)] #length and '(' - ')'
    ans, mod = 0, (10 ** 9) + 7
    dp[1][1] = 1
    
    for i in range(1, 2 * n):
        for j in range(2 * n):
            dp[i + 1][j + 1] += dp[i][j]  #when '(' is appended
            if dp[i + 1][j + 1] >= mod:
                dp[i + 1][j + 1] -= mod
    
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]  #when ')' is appended
                if dp[i + 1][j - 1] >= mod:
                    dp[i + 1][j - 1] -= mod
    
    for i in range(1, 2 * n, 2):
        for j in range(2 * n):
            valid = i + j <= 2 * n
            if valid:
                ans += dp[i][j]
                if ans >= mod:
                    ans -= mod
    print(ans % mod)