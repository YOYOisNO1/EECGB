def program2064():
    mod = 10 ** 9 + 7
    
    n, k, d = map(int, input().split())
    
    
    dp = [] * 205
    
    for i in range (0, 205):
      dp.append([0, 0])
      
    dp[0][0] = 1
    
    for i in range (0, n + 1):
      for j in range (1, k + 1):
        if j >= d:
          dp[i + j][1] = dp[i + j][1] + dp[i][1] + dp[i][0]
        else:
          dp[i + j][1] += dp[i][1]
          dp[i + j][0] += dp[i][0]
    
    print((dp[n][1]%mod))