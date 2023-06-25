def program2089():
    n,k,d = map(int, input().split())
    
    dp1 = [0]*(n+1)
    dp2 = [0]*(n+1)
    dp1[0] = 1
    for i in range(1,n+1):
    	for j in range(1,min(n,k)+1):
    		dp2[i] += dp2[i-j]
    		if(j < d):
    			dp1[i] += dp1[i-j]
    		else:
    			dp2[i] += dp1[i-j]
    print(dp2[n]%1000000007)