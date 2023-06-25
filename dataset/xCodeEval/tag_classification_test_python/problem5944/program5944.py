    import sys
    
def gcd(a,b):
    	while b > 0:
    		a, b = b, a % b
    	return a
    
def dfs(c):
    	res	= 0
    	current = c
    	while not used[current]:
    		used[current] = True
    		res += 1
    		current = crush[current]
    	if res % 2 == 0:
    		res //= 2
    	return 0 if current != c else res
    
    used = [False] * (int(input()) + 1)
    crush = [0] + [int(i) for i in input().split()]
    ans = 1
    
    for c in xrange(1, len(crush)):
    	if not used[c]:
    		ret = dfs(c)
    		if ret: 
    			ans = (ans * ret) // gcd(ans, ret)
    		else: 
    			print('-1')
    			sys.exit(0)
    
    print(ans)