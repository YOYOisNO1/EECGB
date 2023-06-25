    zeroes = int(input().strip())
    fives = 0
    
    dp = {}
def countfives(n):
    	if dp.get(n, -1) != -1:
    		return dp[n]
    
    	if n % 5 != 0:
    		return 0
    	
    	ret = 1 + countfives(n / 5)
    	dp[n] = ret
    	return ret
    
    i = 1
    ret = []
    
    while fives <= zeroes:
    	f = countfives(i)
    	fives = fives + f
    	
    	if fives == zeroes:
    		ret.append(i)
    	
    	i = i + 1
    
    print(len(ret))
    print(" ".join(str(s) for s in ret))