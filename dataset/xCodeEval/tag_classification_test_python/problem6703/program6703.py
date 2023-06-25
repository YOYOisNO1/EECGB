def solve(n):
    	if(n <= 6):
    		return n
    	cur = 1
    	cnt = 1
    	while 10*cur+1 <= n:
    		cur = 10*cur+1
    		cnt += 1
    	if 10*cur+1-n > n:
    		ans = 0
    		while n >= cur:
    			n -= cur
    			ans += cnt
    		return ans+solve(n)
    	ans1 = solve(10*cur+1-n)+cnt+1
    	op = 10*cur+1-n
    	op += cur
    	if(10*cur+1-op > op):
    		return ans1
    	ans2 = 0
    	while n >= cur:
    		n -= cur
    		ans2 += cnt
    	ans2 += solve(n)
    	return min(ans1,ans2)
    
    print(solve(int(input())))