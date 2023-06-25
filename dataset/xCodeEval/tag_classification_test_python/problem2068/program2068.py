def program2068():
    # cook your dish here
    
    Mod = 1000000007
    n , k, d = map(int,input().split())
    
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    
    dp[0][0] = 1
    
    for i in range(1,n + 1):
        for j in range(1,k + 1):
            if j <= i:
                if j < d: 
                    dp[i][0] = (dp[i - j][0] + dp[i][0]) % Mod
                    dp[i][1] = (dp[i - j][1] + dp[i][1]) % Mod
                else:
                    dp[i][1] = (dp[i][1] + dp[i - j][0] + dp[i - j][1]) % Mod
    
    print(dp[n][1])                