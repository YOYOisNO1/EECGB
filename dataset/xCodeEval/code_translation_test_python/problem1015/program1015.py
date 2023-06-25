    import sys
    
    from collections import Counter
    
def distinct_factors(n):
    	ans = 1
    	for x in range(2, n):
    		ans += (n%x == 0)
    	return ans
    
def main():
    	n = int(input())
    
    	mod = 998244353
    
    	dp = [-1]*(n+1)
    
    	pre = 0
    
    	d = [0]*(n+1)
    
    	for i in range(1, n+1):
    		for j in range(i, n+1, i):
    			d[j] += 1
    
    	for i in range(1, n+1):
    		dp[i] = (pre+d[i])%mod
    		pre += dp[i]
    
    
    	return (dp[n])%mod 
    
    print(main())