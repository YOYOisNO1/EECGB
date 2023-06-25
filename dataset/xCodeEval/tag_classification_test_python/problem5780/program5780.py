def program5780():
    n = int(input())
    s = input()
    dp = [[int(1e9)]*n for i in range(n)]
    for i in range(n):
    	dp[i][i] = 1
    for l in range(1,n):
    	for i in range(n-l):
    		j = i + l
    		d = int(1e9)
    		for k in range(i,j):
    			d = min(d, dp[i][k]+dp[k+1][j]-(s[i]==s[k+1]))
    		dp[i][j] = d
    #print(*dp,sep='\n')
    print(dp[0][n-1])