def solve(n):
    	if n <= 6: return n
    	cur = 1
    	cnt = 1
    	while 10*cur+1 <= n:
    		cur = 10*cur+1
    		cnt += 1
    	if n <= 5*cur: return cnt+solve(n-cur)
    	if n > 6*cur: return cnt+1+solve(10*cur+1-n)
    	return min(cnt+solve(n-cur),cnt+1+solve(10*cur+1-n))
    print(solve(int(input())))