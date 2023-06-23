def program4754():
    inf = float('inf')
    
    N,S,K = map(int,input().strip('\n').split(' '))
    A = map(int,input().strip('\n').split(' '))
    color = input().strip('\n')
    
    
    dp = [[inf]*(N+5) for k in range(K+5)]
    for i in range(N):
        dp[A[i]][i] = abs(S-i-1);
    
    for k in range(K+5):
        for pos in range(N):
            if dp[k][pos] == inf:
                continue
            for newpos in range(N):
                if A[newpos]<=A[pos] or color[newpos] == color[pos]:
                    continue
                if k+A[newpos]>K+5:
                    continue
                dp[k+A[newpos]][newpos] = min(dp[k+A[newpos]][newpos], dp[k][pos]+abs(newpos-pos))
    
    
    ans = int(1e18)
    for k in range(K,K+5):
        for pos in range(N):
            ans = min(ans,dp[k][pos])
    print ans
    
    
    
    
    
    # dp = (mintime,last_j,last_c)
    # candies = [(ni,ji,ci)]
    # dp[0][0][1] = S
    # dp[i][k+ni][0] = {c!=ci  dp[i-1][k][0] + dp[i-1][k][1]-j)
    # dp[i][k+ni][1] = j  
    # dp[i][k+ni][2] = c 
    
    # candies = [(n,j,c) for j,(n,c) in enumerate(zip(A,color))]
    # candies = sorted(candies,key=lambda x:x[0])
    
    # dp = []
    # for i in range(N+5):
    #     temp = []
    #     for j in range(K+5):
    #         temp.append([inf,0,0])
    #     dp.append(temp)
    
    # for i in range(N+1):
    #     dp[i][0][0] = 0
    #     dp[i][0][1] = S
    
    # for i in range(1,N+1):
    #     ni,ji,ci = candies[i-1]
    #     for k in range(K+5): 
    #         if k<ni:
    #             continue
    #         if dp[i-1][k][2] != ci:
    #             dp[i][k][0]  = min(dp[i][k][0], dp[i-1][k-ni][0] + abs(dp[i-1][k-ni][1]-j))
    #             dp[i][k][1] = ji  
    #             dp[i][k][2] = ci
    #         else:
    #             dp[i][k][0] = dp[i-1][k][0] + abs(dp[i-1][k][1]-j)
    
    
    # print dp[N]