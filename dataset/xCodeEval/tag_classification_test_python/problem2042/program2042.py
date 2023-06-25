def main():
    	n, k, d = map(int, input().split())
    	mod = 10 ** 9 + 7
    	dp = [0] * (n + 1)
    	dp[0] = 1
    	for i in range(1, n + 1):
    		for j in range(1, k + 1):
    			if i >= j:
    				dp[i] += (dp[i - j] % mod)
    			else:
    				break
    		dp[i] = dp[i] % mod
    	if d == 1:
    		print(dp[n])
    	else:
    		dpl = [0] * (n + 1)
    		dpl[0] = 1
    		for i in range(1, n + 1):
    			for j in range(1, d):
    				 if i >= j:
    					 dpl[i] += dpl[i - j]
    			dpl[i] = dpl[i] % mod
    		print((dp[n] - dpl[n]) % mod)
    		
    
    if __name__ == '__main__':
    	main()