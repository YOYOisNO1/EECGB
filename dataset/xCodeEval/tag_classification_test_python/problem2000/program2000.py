    from array import *
    
def kTree(n,a,d):
    	dp = {}
    	i=0
    	while i<=n:
    		dp[0,i] = 0
    		dp[1,i] = 1
    		i+=1
    
    	i=2
    	while i<=a:		
    		dp[i,0]=1
    		j=1
    		while j<=n:
    			if i>j:
    				dp[i,j] = dp[i-1,j]
    			elif i==j:
    				dp[i,j] = (dp[i-1,j] + dp[i,0])%1000000007
    			else:
    				l=i
    				dp[i,j] =0
    				while l>0:
    					dp[i,j] =(dp[i,j] + dp[i,j-l])%1000000007
    					l-=1
    			j+=1
    		#print(dp)
    		i+=1
    
    	print((dp[k,n]-dp[d-1,n])%1000000007)
    	
    
    
    n,k,d = [int(x) for x in input().split()]
    kTree(n,k,d)