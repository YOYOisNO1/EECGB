    '''input
    3
    '''
    from sys import stdin
    import math
    
    
def make_dp():
    	dp = [0] * 1001
    	dp[1] = 1
    	dp[3] = 5
    	for i in range(5, 100, 2):
    		dp[i] = dp[i - 2] + i + i - 2
    	
    	return dp
    
    # main starts
    x = int(stdin.readline().strip())
    
    if x == 3:
    	print(5)
    	exit()
    dp = make_dp()
    for i in range(1, len(dp)):
    	if x <= dp[i]:
    		print(i)
    		break