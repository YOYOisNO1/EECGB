def program2118():
    n, k, d = input().split()
    n, k, d, = int(n), int(k), int(d)
    mod = 10**9 + 7
    
    dp = [1]
    
    for i in range(1, n + 1):
        
        if i == 1: dp.append(1)
        else:
            dp.append(0)
            
            for j in range(1, min(k, i) + 1):
                dp[-1] += dp[i - j]
                
            dp[-1] %= mod
            
    DP = [0]
    
    for i in range(1, n + 1):
        if i < d: DP.append(0)
        else:
            DP.append(0)
            for j in range(1, min(k, i) + 1):
                
                if j < d:
                    DP[-1] += DP[i - j]
                else: 
                    DP[-1] += dp[i - j]
                    
            DP[-1] %= mod
                
    print(DP[-1])