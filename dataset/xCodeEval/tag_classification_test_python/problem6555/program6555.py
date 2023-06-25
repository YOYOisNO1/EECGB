def program6555():
    range=xrange
    mod=1000000007
    n=int(input())
    m=n*2
    dp=[ [ [0,0] for j in range(n+1)] for k in range(m+1)]
    dp[0][0][0]=0
    dp[0][0][1]=1
    for i in range(1,m+1):
    	for j in range(0,min(m-i,n)+1):
    		Sum=0
    		ok=0
    		if j>0:
    			Sum=(Sum+dp[i-1][j-1][0])%mod
    			ok=ok|(bool(dp[i-1][j-1][1]))
    		if j<i-1:
    			Sum=(Sum+dp[i-1][j+1][0])%mod
    			ok=ok|(bool(dp[i-1][j+1][1]))
    		Sum=(Sum+ok)%mod
    		dp[i][j][0]=Sum
    		dp[i][j][1]=(not ok)
    print(int(dp[m][0][0]))