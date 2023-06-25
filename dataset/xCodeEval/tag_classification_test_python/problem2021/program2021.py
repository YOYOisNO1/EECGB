def program2021():
    n,k,d = map(int,input().split())
    
    dp = [[0]*2 for i in range(n+2)]
    
    dp[0][0] = 1
    
    for i in range(1,n+1):
    	for j in range(1,k+1):
    		if j > i :
    			break
    		if j < d :
    			dp[i][0] = (dp[i-j][0]+dp[i][0])%1000000007
    			dp[i][1] = (dp[i-j][1]+dp[i][1])%1000000007
    		else :
    			dp[i][1] = (dp[i-j][0]+dp[i][1])%1000000007
    			dp[i][1] = (dp[i-j][1]+dp[i][1])%1000000007
    	
    print(dp[n][1])